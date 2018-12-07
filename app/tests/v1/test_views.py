import unittest
from flask import json
from app import create_app
from instance.config import TestingConfig

from app.api.v1.models.incidents import incidents_list


class IncidentTest(unittest.TestCase):
    def setUp(self):
        self.incident = {
            "incidentType": "redflag",
            "comment": "kskksd jieioe sksjlsjdal snskmnlks sjhnjksnkla",
            "createdBy": 8,
            "location": "nairobi"
        }
        self.app = create_app(config_name=TestingConfig)
        self.client = self.app.test_client()

    def create_test_record(self):
        self.client.post('/api/v1/incidents', data=json.dumps(self.incident), content_type='application/json')

    def test_create_incident_success(self):
        resp = self.client.post('/api/v1/incidents', data=json.dumps(self.incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['data'][0]['incidentType'], 'redflag')

    def test_incidentType_should_contain_letters_only(self):
        incident = {
            "incidentType": "redflag$$",
            "comment": "kskksd jieioe sksjlsjdal snskmnlks sjhnjksnkla",
            "createdBy": 8,
            "location": "nairobi"
        }
        resp = self.client.post('/api/v1/incidents', data=json.dumps(incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['message'], 'incidentType can only contain letters only')

    def test_provide_all_the_required_fields(self):
        incident = {
            "incidentType": "redflag",
            "createdBy": 8,
            "location": "nairobi"
        }
        resp = self.client.post('/api/v1/incidents', data=json.dumps(incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['message'], "please provide all the fields, missing 'comment'")

    def test_incidentType_should_be_more_than_7_letters(self):
        incident = {
            "incidentType": "red",
            "comment": "kskksd jieioe sksjlsjdal snskmnlks sjhnjksnkla",
            "createdBy": 8,
            "location": "nairobi"
        }
        resp = self.client.post('/api/v1/incidents', data=json.dumps(incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['message'], 'incidentType must be more than 7 characters')

    def test_comment_should_be_more_than_15_characters(self):
        incident = {
            "incidentType": "redflag",
            "comment": "",
            "createdBy": 8,
            "location": "nairobi"
        }
        resp = self.client.post('/api/v1/incidents', data=json.dumps(incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['message'], 'comment must be more than 15 characters')

    def test_location_should_be_more_than_3_characters(self):
        incident = {
            "incidentType": "redflag",
            "comment": "hjjkjlk lk;ll';l lkl;ko gfhgfuy jhkjn hnbkjh",
            "createdBy": 8,
            "location": "n"
        }
        resp = self.client.post('/api/v1/incidents', data=json.dumps(incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['message'], 'location must be more than 3 characters')
                                    
    def test_createdBy_must_be_an_integer(self):
        incident = {
            "incidentType": "redflag",
            "comment": "hjjkjlk lk;ll';l lkl;ko gfhgfuy jhkjn hnbkjh",
            "createdBy": "ne",
            "location": "nairobi"
        }
        resp = self.client.post('/api/v1/incidents', data=json.dumps(incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['message'], 'createdby must be an integer')
        
    def test_incident_id_increments_correctly(self):
        self.client.post('/api/v1/incidents', data=json.dumps(self.incident), content_type='application/json')
        resp = self.client.post('/api/v1/incidents', data=json.dumps(self.incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['data'][0]['id'], 2)
        self.assertEqual(len(incidents_list), 2)

    def test_can_get_all_incidents(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/incidents')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data'][0]['id'],1 )

    def test_can_patch_an_incident_location(self):
        self.create_test_record()
        patch_data = {
            "location": "mombasa"
        }
        resp = self.client.patch('/api/v1/incidents/1/location', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 202)
        self.assertEqual(data['data'][0]['location'], 'mombasa')

    def test_can_not_patch_if_attribute_not_in_patch_attributes(self):
        self.create_test_record()
        patch_data = {
            "incidentType": "redflag"
        }
        resp = self.client.patch('/api/v1/incidents/1/incidentType', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['message'], 'You can only patch location or comment.')

    def test_can_patch_an_incident_comment(self):
        self.create_test_record()
        patch_data = {
            "comment": "I have just updated this comment"
        }
        resp = self.client.patch('/api/v1/incidents/1/comment', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 202)
        self.assertEqual(data['data'][0]['comment'], 'I have just updated this comment')

    def test_cannot_patch_an_empty_incident_comment(self):
        self.create_test_record()
        patch_data = {
            "comment": ""
        }
        resp = self.client.patch('/api/v1/incidents/1/comment', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['data'][0]['error'], 'Comment should be more than 15 characters')
    
    def test_cannot_patch_an_empty_incident_location(self):
        self.create_test_record()
        patch_data = {
            "location": ""
        }
        resp = self.client.patch('/api/v1/incidents/1/location', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 400)
        self.assertEqual(data['data'][0]['error'], 'Location should be more than 3 characters')

    def test_can_get_incident_by_id(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/incidents/1')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(incidents_list), 1)
        self.assertEqual(data['data'][0]['id'],1 )

    def test_get_non_existent_incident(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/incidents/10')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['message'], 'Record with that ID does not exist.')

    def test_get_incident_by_id_with_special_character(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/incidents/7!')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['error'], 'The record you are looking for does not exist')

    def test_can_delete_incident(self):
        self.create_test_record()
        resp = self.client.delete('/api/v1/incidents/1')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'], 'The record has been deleted')
        resp = self.client.get('/api/v1/incidents/1')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(data['message'], 'Record with that ID does not exist.')   

    def tearDown(self):
        incidents_list.clear()
