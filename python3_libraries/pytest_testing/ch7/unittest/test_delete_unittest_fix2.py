import pytest
import unittest
import tasks
from tasks import Task


@pytest.fixture()
def tasks_db_non_empty(tasks_db_session, request):
    tasks.delete_all()  # start empty
    # add a few items, saving ids
    ids = []
    ids.append(tasks.add(Task('One', 'Brian', True)))
    ids.append(tasks.add(Task('Two', 'Still Brian', False)))
    ids.append(tasks.add(Task('Three', 'Not Brian', False)))
    request.cls.ids = ids


@pytest.mark.usefixtures('tasks_db_non_empty')
class TestNonEmpty(unittest.TestCase):

    def test_delete_decreases_count(self):
        # GIVEN 3 items
        self.assertEqual(tasks.count(), 3)
        # WHEN we delete one
        tasks.delete(self.ids[0])
        # THEN count decreases by 1
        self.assertEqual(tasks.count(), 2)
