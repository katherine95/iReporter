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
            "phonenumber": "07975554444"
        }
        config_name = "testing"
        self.app = create_app(config_name)
        self.client = self.app.test_client()
        create_tables()

    def create_test_record(self):
        self.client.post(
            '/api/v2/users', data=json.dumps(self.user),
            content_type='application/json')

    def test_create_user_success(self):
        resp = self.client.post(
            '/api/v2/users', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(data['data']['username'], 'testusername')

    def test_username_taken(self):
        self.create_test_record()
        resp = self.client.post(
            '/api/v2/users', data=json.dumps(self.user),
            content_type='application/json')
        data = json.loads(resp.data)
        self.assertEqual(resp.status_code, 409)
        self.assertEqual(data['message'], 'Username Is already taken')

    def tearDown(self):
        create_tables()
