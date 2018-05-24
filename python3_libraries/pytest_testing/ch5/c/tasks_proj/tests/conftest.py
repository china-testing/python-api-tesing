"""Define some fixtures to use in the project."""

import pytest
import tasks
from tasks import Task


@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory, request):
    """Connect to db before tests, disconnect after."""
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield  # this is where the testing happens
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(tasks_db_session):
    """An empty tasks db."""
    tasks.delete_all()


# Reminder of Task constructor interface
# Task(summary=None, owner=None, done=False, id=None)
# Don't set id, it's set by database
# owner and done are optional


@pytest.fixture()
def tasks_just_a_few():
    """All summaries and owners are unique."""
    return (
        Task('Write some code', 'Brian', True),
        Task("Code review Brian's code", 'Katie', False),
        Task('Fix what Brian did', 'Michelle', False))


@pytest.fixture()
def tasks_mult_per_owner():
    """Several owners with several tasks each."""
    return (
        Task('Make a cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Berlin', 'Raphael'),

        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),

        Task('Do a handstand', 'Daniel'),
        Task('Write some books', 'Daniel'),
        Task('Eat ice cream', 'Daniel'))


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    """Connected db with 3 tasks, all unique."""
    for t in tasks_just_a_few:
        tasks.add(t)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    """Connected db with 9 tasks, 3 owners, all with 3 tasks."""
    for t in tasks_mult_per_owner:
        tasks.add(t)


def pytest_addoption(parser):
    """Turn nice features on with --nice option."""
    group = parser.getgroup('nice')
    group.addoption("--nice", action="store_true",
                    help="nice: turn failures into opportunities")


def pytest_report_header():
    """Thank tester for running tests."""
    if pytest.config.getoption('nice'):
        return "Thanks for running the tests."


def pytest_report_teststatus(report):
    """Turn failures into opportunities."""
    if report.when == 'call':
        if report.failed and pytest.config.getoption('nice'):
            return (report.outcome, 'O', 'OPPORTUNITY for improvement')
