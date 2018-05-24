"""Test tasks.unique_id()."""

import tasks


def test_unique_id(tasks_db, tasks_mult_per_owner):
    """unique_id() should return an unused id."""
    existing_tasks = tasks.list_tasks()
    uid = tasks.unique_id()
    for t in existing_tasks:
        assert uid != t.id
