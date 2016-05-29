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

    def test_get_folders(self):
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetFolders()

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue(len(results), 2)
        self.assertTrue('title' in results[0])

    def test_get_folder(self):
        folder_id = "7654321"

        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetFolders(folder_id=folder_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('id' in results)
        self.assertTrue('title' in results)
        self.assertTrue('list_ids' in results)

    def test_get_lists(self):
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetLists()

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue(len(results), 2)
        self.assertTrue('title' in results[0])
        self.assertTrue('title' in results[1])

    def test_get_lists_list_id(self):
        list_id = "12345678"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetLists(list_id=list_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('id' in results)
        self.assertTrue('title' in results)

    def test_get_notes_no_param(self):
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetNotes()

        self.assertEqual(results, None)

    def test_get_notes_task_id(self):
        task_id = "1234567890"

        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetNotes(task_id=task_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue(len(results), 1)
        self.assertTrue('content' in results[0])
        self.assertEqual(results[0]['type'], 'note')

    def test_get_notes_list_id(self):
        list_id = "12345678"

        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetNotes(list_id=list_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue(len(results), 1)
        self.assertTrue('content' in results[0])
        self.assertEqual(results[0]['type'], 'note')

    def test_get_notes_note_id(self):
        note_id = "123456789"

        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetNotes(note_id=note_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('content' in results)
        self.assertEqual(results['type'], 'note')

if __name__ == '__main__':
    unittest.main()
