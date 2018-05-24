"""Database wrapper for MongoDB for tasks project."""

import os
import pymongo
import subprocess
import time
from bson.objectid import ObjectId


class TasksDB_MongoDB():  # noqa: E801
    """Wrapper class for MongoDB.

    The methods in this class need to match
    all database interaction classes.

    So far, this is:
    TasksDB_TinyDB found in tasksdb_tinydb.py.
    """

    def __init__(self, db_path):  # type (str) -> ()
        """Start MongoDB client and connect to db."""
        self._process = None
        self._client = None
        self._start_mongod(db_path)
        self._connect()

    def add(self, task):  # type (dict) -> int
        """Add a task dict to db."""
        return self._db.task_list.insert_one(task).inserted_id

    def get(self, task_id):  # type (int) -> dict
        """Return a task dict with matching id."""
        return self._db.task_list.find_one({'_id': ObjectId(task_id)})

    def list_tasks(self, owner=None):  # type (str) -> list[dict]
        """Return list of tasks."""
        return list(self._db.task_list.find())

    def count(self):  # type () -> int
        """Return number of tasks in db."""
        return self._db.task_list.count()

    def update(self, task_id, task):  # type (int, dict) -> ()
        """Modify task in db with given task_id."""
        self._db.tasks_list.update_one({'_id': ObjectId(task_id)}, task)

    def delete(self, task_id):  # type (int) -> ()
        """Remove a task from db with given task_id."""
        reply = self._db.task_list.delete_one({'_id': ObjectId(task_id)})
        if reply.deleted_count == 0:
            raise ValueError('id {} not in task database'.format(str(task_id)))

    def unique_id(self):  # type () -> int
        """Return an integer that does not exist in the db."""
        return ObjectId()

    def delete_all(self):
        """Remove all tasks from db."""
        self._db.task_list.drop()

    def stop_tasks_db(self):
        """Disconnect from db."""
        self._disconnect()
        self._stop_mongod()

    def _start_mongod(self, db_path):
        self._process = subprocess.Popen(['mongod', '--dbpath', db_path],
                                         stdout=open(os.devnull, 'wb'),
                                         stderr=subprocess.STDOUT)
        assert self._process, "mongod process failed to start"

    def _stop_mongod(self):
        if self._process:
            self._process.terminate()
            self._process.wait()
            self._process = None

    def _connect(self):
        if self._process and (not self._client or not self._db):
            for i in range(3):
                try:
                    self._client = pymongo.MongoClient()
                except pymongo.errors.ConnectionFailure:
                    time.sleep(0.1)
                    continue
                else:
                    break
            if self._client:
                self._db = self._client.task_list

    def _disconnect(self):
        self._db = None
        self._client = None


def start_tasks_db(db_path):  # type (str) -> TasksDB_MongoDB object
    """Connect to db."""
    return TasksDB_MongoDB(db_path)
