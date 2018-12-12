import os
import unittest
from flask import json
from app import create_app
from instance.config import TestingConfig

from app.api.v1.models.incidents import incidents_list
from migrate import create_tables


class UserTest(unittest.TestCase):
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
        self.incident = {
            "incidentType": "redflag",
            "location": "36N",
            "comment": "hjjkjklkllkls hjkjlj kjhkjj jhkjn",
            "createdBy": 1
        }
        config_name = "testing"
        self.app = create_app(config_name)
        self.client = self.app.test_client()
        create_tables()

    def create_test_user(self):
        self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user),
            content_type='application/json')

    def create_test_record(self):
        self.client.post(
            '/api/v2/incidents', data=json.dumps(self.incident),
            content_type='application/json')

    def test_create_user_success(self):
        resp = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['data'][0]['user']['username'], 'testusername')

    def test_username_taken(self):
        self.create_test_user()
        resp = self.client.post(
            '/api/v2/auth/signup', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        import pdb
        self.assertEqual(resp.status_code, 409)
        self.assertEqual(data['message'], 'Username Is already taken')

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

    # def test_require_auth_to_request_endpoints(self):
    #     self.create_test_user()
    #     resp = self.client.post(
    #         '/api/v2/auth/login', data=json.dumps(self.user),
    #         content_type='application/json')
    #     data = json.loads(resp.data)
    #     access_token = data['data'][0]['token']
    #     Authorization = 'Bearer ' + access_token
    #     headers = {'content-type': 'application/json',
    #                'Authorization': Authorization}
    #     resp = self.client.post(
    #         '/api/v2/incidents', data=json.dumps(self.incident),
    #         content_type='application/json', headers=headers)
    #     data = json.loads(resp.data)
    #     self.assertEqual(resp.status_code, 401)
    #     self.assertEqual(data['msg'], "Token has expired")

    def test_create_incident_success(self):
        self.create_test_user()
        resp = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        access_token = data['data'][0]['token']
        Authorization = 'Bearer ' + access_token
        headers = {'content-type': 'application/json',
                   'Authorization': Authorization}
        resp = self.client.post(
            '/api/v2/incidents', data=json.dumps(self.incident),
            content_type='application/json', headers=headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['data'][0]['message'], 'Incident created'
                         ' successfully.')

    def test_if_incident_with_same_comment_exists(self):
        self.create_test_user()
        resp = self.client.post(
            '/api/v2/auth/login', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        access_token = data['data'][0]['token']
        Authorization = 'Bearer ' + access_token
        headers = {'content-type': 'application/json',
                   'Authorization': Authorization}
        resp = self.client.post(
            '/api/v1/incidents', data=json.dumps(self.incident),
            content_type='application/json', headers=headers)
        resp = self.client.post(
            '/api/v1/incidents', data=json.dumps(self.incident),
            content_type='application/json', headers=headers)
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 409)
        self.assertEqual(data['message'], 'Incident with this comment exist.')

    def tearDown(self):
        create_tables()
