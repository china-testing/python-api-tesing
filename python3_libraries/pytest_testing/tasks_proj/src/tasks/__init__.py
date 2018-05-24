"""Minimal Project Task Management."""

from .api import (  # noqa: F401
    Task,
    TasksException,
    add,
    get,
    list_tasks,
    count,
    update,
    delete,
    delete_all,
    unique_id,
    start_tasks_db,
    stop_tasks_db
)

__version__ = '0.1.0'
