import os
import unittest
from flask import json
from app import create_app
from instance.config import TestingConfig

from app.api.v1.models.incidents import incidents_list
from migrate import create_tables


class TestView(unittest.TestCase):
    def setUp(self):
        self.user = {
            "username": "testusername",
            "email": "test@gmail.com",
            "password": "pass123.",
            "firstname": "cate",
            "lastname": "chepc",
            "othernames": "plum",
            "phonenumber": "0797555444"
        }
        self.user2 = {
            "username": "testusernamer",
            "email": "test3@gmail.com",
            "password": "pass123.",
            "firstname": "cate",
            "lastname": "chepc",
            "othernames": "plum",
            "phonenumber": "0797555444"
        }
        self.user3 = {
            "username": "testusername",
            "email": "test36@gmail.com",
            "password": "pass123.",
            "firstname": "cate",
            "lastname": "chepc",
            "othernames": "plum",
            "phonenumber": "0797555444"
        }
        self.incident = {
            "incidentType": "Redflag",
            "location": "36N",
            "comment": "hjjkjklkllkls hjkjlj kjhkjjkjkxlkj jhkjn",
        }
        config_name = "testing"
        self.app = create_app(config_name)
        self.client = self.app.test_client()
        create_tables()

        self.test_user = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user2),
            content_type='application/json')
        self.incident_data = json.loads(self.test_user.data)
        self.access_token = self.incident_data['data'][0]['token']
        self.Authorization = 'Bearer ' + self.access_token
        self.headers = {'content-type': 'application/json',
                        'Authorization': self.Authorization}

    def create_test_record(self):
        return self.client.post(
            '/api/v2/incidents', data=json.dumps(self.incident),
            content_type='application/json', headers=self.headers)

    def create_test_user(self):
        return self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user),
            content_type='application/json')

    def test_create_user_success(self):
        resp = self.create_test_user()
        print('user response' + str(resp))
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['data'][0]['user']['username'], 'testusername')

    def test_username_taken(self):
        self.create_test_user()
        resp = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user3),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 409)
        self.assertEqual(data['message'], 'Username Is already taken')

    def test_email_taken(self):
        self.create_test_user()
        resp = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 409)
        self.assertEqual(data['message'], 'Email is already taken')

    def test_user_log_in_success(self):
        self.create_test_user()
        resp = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data'][0]['user']['username'], 'testusername')

    def test_user_login_token_generation_success(self):
        self.create_test_user()
        resp = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(data['data'][0]['token'])

    def test_login_with_wrong_credentials(self):
        self.create_test_user()
        user = {
            "username": "testusername",
            "password": "pass12"
        }
        resp = self.client.post(
            '/api/v2/auth/login', data=json.dumps(user),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['message'], 'Username and password dont match')

    def test_require_authorization_with_access_token(self):
        resp = self.client.post(
            '/api/v2/incidents', data=json.dumps(self.incident),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(data['msg'], 'Missing Authorization Header')

    def test_provide_all_the_required_fields(self):
        incident = {
            "incidentType": "Redflag",
            "location": "nairobi"
        }
        resp = self.client.post(
            '/api/v2/incidents', data=json.dumps(incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            data['message'],
            "please provide all the fields, missing 'comment'")

    def test_comment_should_be_more_than_15_characters(self):
        incident = {
            "incidentType": "Redflag",
            "comment": "",
            "location": "nairobi"
        }
        resp = self.client.post(
            '/api/v2/incidents', data=json.dumps(incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            data['message'], 'comment must be more than 15 characters')

    def test_location_should_be_more_than_3_characters(self):
        incident = {
            "incidentType": "Redflag",
            "comment": "hjjkjlk lk;ll';l lkl;ko gfhgfuy jhkjn hnbkjh",
            "location": "n"
        }
        resp = self.client.post(
            '/api/v2/incidents', data=json.dumps(incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(
            data['message'], 'location must be more than 3 characters')

    def test_create_incident_success(self):
        resp = self.create_test_record()
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['data'][0]['message'], 'Incident created'
                         ' successfully.')

    def test_if_incident_with_same_comment_exists(self):
        self.create_test_record()
        resp = self.client.post(
            '/api/v2/incidents', data=json.dumps(self.incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 409)
        self.assertEqual(data['message'], 'Incident with this comment exist.')

    def test_can_get_all_incidents(self):
        self.create_test_record()
        resp = self.client.get(
            '/api/v2/incidents', data=json.dumps(self.incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(data['data']), 1)

    def test_can_get_incident_by_id(self):
        self.create_test_record()
        resp = self.client.get(
            '/api/v2/incidents/1', data=json.dumps(self.incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data']['id'], 1)

    def test_cannot_get_incident_by_non_existing_id(self):
        self.create_test_record()
        resp = self.client.get(
            '/api/v2/incidents/4', data=json.dumps(self.incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['message'],
                         'Record with that ID does not exist.')

    def test_admin_can_update_record_status(self):
        self.create_test_record()
        admin = {
            'username': 'catechep',
            'password': 'Cate@95#'
        }
        admin_login = self.client.post(
            '/api/v2/auth/login', data=json.dumps(admin),
            content_type='application/json')
        data = json.loads(admin_login.data)
        access_token = data['data'][0]['token']
        Authorization = 'Bearer ' + access_token
        headers = {'content-type': 'application/json',
                   'Authorization': Authorization}
        patch_data = {
            'status': 'inDraft'
        }
        resp = self.client.patch(
            '/api/v2/incidents/1', data=json.dumps(patch_data),
            content_type='application/json', headers=headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'], 'Incident patched successfully')

    def test_only_admin_update_record_status(self):
        self.create_test_record()
        patch_data = {
            'status': 'inDraft'
        }
        resp = self.client.patch(
            '/api/v2/incidents/1', data=json.dumps(patch_data),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(data['message'], 'you dont have access rights')

    def test_admin_can_create_new_admin(self):
        self.create_test_user()
        admin = {
            'username': 'catechep',
            'password': 'Cate@95#'
        }
        admin_login = self.client.post(
            '/api/v2/auth/login', data=json.dumps(admin),
            content_type='application/json')
        data = json.loads(admin_login.data)
        access_token = data['data'][0]['token']
        Authorization = 'Bearer ' + access_token
        headers = {'content-type': 'application/json',
                   'Authorization': Authorization}
        patch_data = {
            'isAdmin': 'True'
        }
        resp = self.client.patch(
            'api/v2/auth/users/testusername', data=json.dumps(patch_data),
            content_type='application/json', headers=headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data']['isAdmin'], True)

    def test_only_admin_can_create_new_admin(self):
        self.create_test_user()
        patch_data = {
            'isAdmin': 'True'
        }
        resp = self.client.patch(
            '/api/v2/auth/users/testusername', data=json.dumps(patch_data),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(data['message'], 'you dont have access rights')

    def test_admin_can_get_all_users(self):
        self.create_test_user()
        admin = {
            'username': 'catechep',
            'password': 'Cate@95#'
        }
        admin_login = self.client.post(
            '/api/v2/auth/login', data=json.dumps(admin),
            content_type='application/json')
        data = json.loads(admin_login.data)
        access_token = data['data'][0]['token']
        Authorization = 'Bearer ' + access_token
        headers = {'content-type': 'application/json',
                   'Authorization': Authorization}
        resp = self.client.get(
            '/api/v2/auth/signup',
            content_type='application/json', headers=headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'], 'all users fetched successfully')

    def test_can_patch_an_incident_comment(self):
        self.create_test_record()
        patch_data = {
            'comment': 'I have just updated this comment sjhakjsh'
        }
        resp = self.client.patch('/api/v2/user/incidents/1',
                                 data=json.dumps(patch_data),
                                 content_type='application/json',
                                 headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'],
                         'Comment patched successfully')

    def test_can_patch_an_incident_location(self):
        self.create_test_record()
        patch_data = {
            'location': '74n'
        }
        resp = self.client.patch('/api/v2/user/incidents/1',
                                 data=json.dumps(patch_data),
                                 content_type='application/json',
                                 headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'],
                         'Location patched successfully')

    def test_cannot_patch_an_incident_when_status_changed(self):
        self.create_test_record()
        admin = {
            'username': 'catechep',
            'password': 'Cate@95#'
        }
        admin_login = self.client.post(
            '/api/v2/auth/login', data=json.dumps(admin),
            content_type='application/json')
        data = json.loads(admin_login.data)
        access_token = data['data'][0]['token']
        Authorization = 'Bearer ' + access_token
        headers = {'content-type': 'application/json',
                   'Authorization': Authorization}
        patch_data = {
            'status': 'inDraft'
        }
        self.client.patch(
            '/api/v2/incidents/1', data=json.dumps(patch_data),
            content_type='application/json', headers=headers)
        incident = {
            "comment": "i changed my mind iiujioj gvytggyghiu yguyhiu yfyughi",
            "createdBy": 1,
            "createdOn": "Fri, 14 Dec 2018 21:00:00 GMT",
            "id": 1,
            "incidentType": "Intervention",
            "location": "36n",
            "status": "inDraft"
        }
        resp = self.client.patch('/api/v2/user/incidents/1',
                                 data=json.dumps(incident),
                                 content_type='application/json',
                                 headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 401)
        self.assertEqual(data['message'],
                         'You can only edit a record while its pending')

    def test_validate_incidentType(self):
        incident = {
            "incidentType": "redflag",
            "location": "36N",
            "comment": "hjjkjklkllkls hjkjlj kjhkjjkjkxlkj jhkjn"
        }
        resp = self.client.post(
            '/api/v2/incidents', data=json.dumps(incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['message'],
                         "incidentType should be 'Redflag' or 'Intervention'")

    def test_can_delete_incident(self):
        self.create_test_record()
        resp = self.client.delete(
            '/api/v2/incidents/1', data=json.dumps(self.incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data'][0]['message'],
                         'Incident deleted successfully')
        resp = self.client.get(
            '/api/v2/incidents/1', data=json.dumps(self.incident),
            content_type='application/json', headers=self.headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['message'],
                         'Record with that ID does not exist.')

    def tearDown(self):
        create_tables()
