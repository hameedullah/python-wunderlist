#!/usr/bin/env python
# −*− coding: UTF−8 −*−

import unittest

from httmock import HTTMock

import wunderlist
import wlmock


class TestWunderlist(unittest.TestCase):
    """Basic Unit Test Class for Wunderlist Class"""

    def setUp(self):
        self.wunderlist = wunderlist.Wunderlist("client_id")
        # TODO: Add Access Token check probably?
        self.wunderlist.setAccessToken("access_token")

    #@with_httmock(wlmock.api_endpoint)
    def test_get_user(self):
        email = 'test@domain.com'

        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetUser()

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertNotEqual(results, {})
        self.assertTrue('id' in results)
        self.assertTrue('name' in results)
        self.assertTrue('email' in results)
        self.assertEqual(results['email'], email)

if __name__ == '__main__':
    unittest.main()
