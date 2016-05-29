#!/usr/bin/env python
# −*− coding: UTF−8 −*−

import unittest

from httmock import HTTMock

import wunderlist
import wlmock

# TODO: Organize End points tests into their own classes

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

    def test_get_folders_folder_id(self):
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

    def test_get_list_positions(self):
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetListPositions()

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('values' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'list_position')

    def test_get_list_positions_id(self):
        pos_id = "2123456"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetListPositions(pos_id=pos_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('values' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'list_position')

    def test_get_task_positions(self):
        list_id="12345678"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetTaskPositions(list_id=list_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('values' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'task_position')

    def test_get_task_positions_id(self):
        pos_id = "31867924"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetTaskPositions(pos_id=pos_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('values' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'task_position')

    def test_get_subtask_positions_list_id(self):
        list_id = "12345678"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetSubTaskPositions(list_id=list_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('values' in results[0])
        self.assertTrue('task_id' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'subtask_position')

    def test_get_subtask_positions_task_id(self):
        task_id = "1795987716"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetSubTaskPositions(task_id=task_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('values' in results[0])
        self.assertTrue('task_id' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'subtask_position')

    def test_get_subtask_positions_id(self):
        pos_id = "1795987716"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetSubTaskPositions(pos_id=pos_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('id' in results)
        self.assertTrue('values' in results)
        self.assertTrue('task_id' in results)
        self.assertTrue('type' in results)
        self.assertEqual(results['type'], 'subtask_position')

    def test_get_reminders_list_id(self):
        list_id = "12345678"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetReminders(list_id=list_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('date' in results[0])
        self.assertTrue('task_id' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'reminder')

    def test_get_reminders_task_id(self):
        task_id = "1795987716"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetReminders(task_id=task_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('date' in results[0])
        self.assertTrue('task_id' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'reminder')

    def test_get_subtasks_list_id(self):
        list_id = "12345678"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetSubTasks(list_id=list_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('title' in results[0])
        self.assertTrue('task_id' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'subtask')

    def test_get_subtasks_task_id(self):
        task_id = "1795987716"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetSubTasks(task_id=task_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('title' in results[0])
        self.assertTrue('task_id' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'subtask')

    def test_get_subtasks_subtask_id(self):
        subtask_id = "1254964618"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetSubTasks(subtask_id=subtask_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('id' in results)
        self.assertTrue('title' in results)
        self.assertTrue('task_id' in results)
        self.assertTrue('type' in results)
        self.assertEqual(results['type'], 'subtask')

    def test_get_tasks_list_id(self):
        list_id = "12345678"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetTasks(list_id=list_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, list)
        self.assertTrue('id' in results[0])
        self.assertTrue('title' in results[0])
        self.assertTrue('list_id' in results[0])
        self.assertTrue('type' in results[0])
        self.assertEqual(results[0]['type'], 'task')

    def test_get_tasks_id(self):
        task_id = "1795987716"
        with HTTMock(wlmock.api_endpoint):
            results = self.wunderlist.GetTasks(task_id=task_id)

        self.assertNotEqual(results, None)
        self.assertIsInstance(results, dict)
        self.assertTrue('id' in results)
        self.assertTrue('title' in results)
        self.assertTrue('list_id' in results)
        self.assertTrue('type' in results)
        self.assertEqual(results['type'], 'task')

if __name__ == '__main__':
    unittest.main()
