"""Database wrapper for MongoDB for tasks project."""

import os
import pymongo
import subprocess
import time


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
        task['_id'] = self._get_next_task_id()
        return self._db.task_list.insert_one(task).inserted_id

    def get(self, task_id):
        """Return a task dict with matching id."""
        task_dict = self._db.task_list.find_one({'_id': task_id})
        task_dict['id'] = task_dict.pop('_id')
        return task_dict

    def list_tasks(self, owner=None):  # type (str) -> list[dict]
        """Return list of tasks."""
        if owner is None:
            all = self._db.task_list.find()
        else:
            all = self._db.task_list.find({'owner': owner})
        for task_dict in all:
            task_dict['id'] = task_dict.pop('_id')
        return all

    def count(self):  # type () -> int
        """Return number of tasks in db."""
        return self._db.task_list.count()

    def update(self, task_id, task):  # type (int, dict) -> ()
        """Modify task in db with given task_id."""
        self._db.tasks_list.update_one({'_id': task_id}, task)

    def delete(self, task_id):  # type (int) -> ()
        """Remove a task from db with given task_id."""
        reply = self._db.task_list.delete_one({'_id': task_id})
        if reply.deleted_count == 0:
            raise ValueError('id {} not in task database'.format(str(task_id)))

    def unique_id(self):  # type () -> int
        """Return an integer that does not exist in the db."""
        tail_task_ids = self._db.counters.find_one({'_id': 'tasksid'})
        uid = tail_task_ids['seq'] + 1
        return uid

    def delete_all(self):
        """Remove all tasks from db."""
        self._db.task_list.drop()

    def stop_tasks_db(self):
        """Disconnect from db."""
        self._disconnect()
        self._stop_mongod()

    def _start_mongod(self, db_path):
        self._devnull = open(os.devnull, 'wb')
        self._process = subprocess.Popen(['mongod', '--dbpath', db_path],
                                         stdout=self._devnull,
                                         stderr=subprocess.STDOUT)
        assert self._process, "mongod process failed to start"

    def _stop_mongod(self):
        if self._client:
            self._client = None
        if self._process:
            self._process.terminate()
            self._process.wait()
            self._devnull.close()
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
                self._db = self._client.task_db
                self._db.counters.insert_one({'_id': 'tasksid', 'seq': 0})

    def _reset_task_id(self):
        self._db.counters.find_one_and_update({'_id': 'tasksid'},
                                              {'$set': {'seq': 0}})

    def _get_next_task_id(self):
        ret = self._db.counters.find_one_and_update({'_id': 'tasksid'},
                                                    {'$inc': {'seq': 1}})
        return ret['seq']

    def _disconnect(self):
        self._db = None


def start_tasks_db(db_path):  # type (str) -> TasksDB_MongoDB object
    """Connect to db."""
    return TasksDB_MongoDB(db_path)
