"""Handle configuration files for tasks CLI."""

from collections import namedtuple
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

import os

TasksConfig = namedtuple('TasksConfig', ['db_path', 'db_type'])


def get_config():
    """Return TasksConfig object after reading config file."""
    parser = ConfigParser()
    config_file = os.path.expanduser('~/.tasks.config')
    if not os.path.exists(config_file):
        tasks_db_path = '~/tasks_db/'
        tasks_db_type = 'tiny'
    else:
        parser.read(config_file)
        tasks_db_path = parser.get('TASKS', 'tasks_db_path')
        tasks_db_type = parser.get('TASKS', 'tasks_db_type')
    tasks_db_path = os.path.expanduser(tasks_db_path)
    return TasksConfig(tasks_db_path, tasks_db_type)
