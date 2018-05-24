import pytest
import unittest
import tasks
from tasks import Task


@pytest.mark.usefixtures('tasks_db_session')
class TestNonEmpty(unittest.TestCase):

    def setUp(self):
        tasks.delete_all()  # start empty
        # add a few items, saving ids
        self.ids = []
        self.ids.append(tasks.add(Task('One', 'Brian', True)))
        self.ids.append(tasks.add(Task('Two', 'Still Brian', False)))
        self.ids.append(tasks.add(Task('Three', 'Not Brian', False)))

    def test_delete_decreases_count(self):
        # GIVEN 3 items
        self.assertEqual(tasks.count(), 3)
        # WHEN we delete one
        tasks.delete(self.ids[0])
        # THEN count decreases by 1
        self.assertEqual(tasks.count(), 2)
