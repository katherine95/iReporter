import unittest
from flask import json
from app import create_app

class IncidentTest(unittest.TestCase):
    def setUp(self):
        self.incident = {
            "incidentType": "redflag",
            "comment" : "kskksd jieioe",
            "createdBy" : 8,
            "location" : "nairobi"
        }
        self.app = create_app('testing')
        self.client = self.app.test_client()

    def create_test_record(self):
        self.client.post('/api/v1/incidents', data=json.dumps(self.incident), content_type='application/json')

    def test_create_incident_success(self):
        resp = self.client.post('/api/v1/incidents', data=json.dumps(self.incident), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['message'], "Created succesfully")

    def test_can_get_all_incidents(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/incidents')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(data['incidents']), 1)

    def test_can_patch_a_location(self):
        self.create_test_record()
        patch_data = {
            "location": "mombasa"
        }
        resp = self.client.patch('/api/v1/redflags/1/location', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(data['message'], 'Patched successfully')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(data['data']['location'], 'mombasa')

    def test_can_not_patch_non_existent_record(self):
        self.create_test_record()
        patch_data = {
            "location": "mombasa"
        }
        resp = self.client.patch('/api/v1/redflags/5/location', data=json.dumps(patch_data), content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(data['message'], 'Record with that ID does not exist.')
        self.assertEqual(data['status'], 404)

    def test_can_get_one_incident(self):
        self.create_test_record()
        resp = self.client.get('/api/v1/redflags/1')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 200)
        # self.assertEqual(len(data['incidents']), 1)