import unittest
import shutil
import tempfile
import tasks
from tasks import Task


def setUpModule():
    """Make temp dir, initialize DB."""
    global temp_dir
    temp_dir = tempfile.mkdtemp()
    tasks.start_tasks_db(str(temp_dir), 'tiny')


def tearDownModule():
    """Clean up DB, remove temp dir."""
    tasks.stop_tasks_db()
    shutil.rmtree(temp_dir)


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
