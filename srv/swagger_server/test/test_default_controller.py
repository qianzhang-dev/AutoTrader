# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.alert import Alert  # noqa: E501
from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.body1 import Body1  # noqa: E501
from swagger_server.models.body2 import Body2  # noqa: E501
from swagger_server.models.user import User  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_ping(self):
        """Test case for get_ping

        Healthcheck Endpoint
        """
        response = self.client.open(
            '/ping',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_user_id(self):
        """Test case for get_users_user_id

        Get User Info by User ID
        """
        query_string = [('key', 'key_example')]
        response = self.client.open(
            '/users/{userId}'.format(user_id=56),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_user_id_alerts(self):
        """Test case for get_users_user_id_alerts

        Get all alerts bound to a user
        """
        response = self.client.open(
            '/users/{userId}/alerts'.format(user_id='user_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_user_id_alerts_ticker(self):
        """Test case for get_users_user_id_alerts_ticker

        Get alerts bound to user matches the ticker
        """
        response = self.client.open(
            '/users/{userId}/alerts/{ticker}'.format(user_id='user_id_example', ticker='ticker_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_users_user_id_alerts_ticker_alert_id(self):
        """Test case for get_users_user_id_alerts_ticker_alert_id

        Get a specific alert by id
        """
        response = self.client.open(
            '/users/{userId}/alerts/{ticker}/{alertId}'.format(user_id='user_id_example', ticker='ticker_example', alert_id='alert_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patch_users_user_id(self):
        """Test case for patch_users_user_id

        Update User Information
        """
        body = Body()
        response = self.client.open(
            '/users/{userId}'.format(user_id=56),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_user(self):
        """Test case for post_user

        Create New User
        """
        body = Body1()
        response = self.client.open(
            '/user',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_users_user_id_alert(self):
        """Test case for post_users_user_id_alert

        Create an alert with expected rules
        """
        body = Body2()
        response = self.client.open(
            '/users/{userId}/alert'.format(user_id='user_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
