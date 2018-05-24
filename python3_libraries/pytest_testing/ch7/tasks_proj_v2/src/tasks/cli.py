"""Command Line Interface (CLI) for tasks project."""

from __future__ import print_function
import click
import tasks.config
from contextlib import contextmanager
from tasks.api import Task


# The main entry point for tasks.
@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version='0.1.1')
def tasks_cli():
    """Run the tasks application."""
    pass


@tasks_cli.command(help="add a task")
@click.argument('summary')
@click.option('-o', '--owner', default=None,
              help='set the task owner')
def add(summary, owner):
    """Add a task to db."""
    with _tasks_db():
        tasks.add(Task(summary, owner))


@tasks_cli.command(help="delete a task")
@click.argument('task_id', type=int)
def delete(task_id):
    """Remove task in db with given id."""
    with _tasks_db():
        tasks.delete(task_id)


@tasks_cli.command(name="list", help="list tasks")
@click.option('-o', '--owner', default=None,
              help='list tasks with this owner')
def list_tasks(owner):
    """
    List tasks in db.

    If owner given, only list tasks with that owner.
    """
    formatstr = "{: >4} {: >10} {: >5} {}"
    print(formatstr.format('ID', 'owner', 'done', 'summary'))
    print(formatstr.format('--', '-----', '----', '-------'))
    with _tasks_db():
        for t in tasks.list_tasks(owner):
            done = 'True' if t.done else 'False'
            owner = '' if t.owner is None else t.owner
            print(formatstr.format(
                  t.id, owner, done, t.summary))


@tasks_cli.command(help="update task")
@click.argument('task_id', type=int)
@click.option('-o', '--owner', default=None,
              help='change the task owner')
@click.option('-s', '--summary', default=None,
              help='change the task summary')
@click.option('-d', '--done', default=None,
              type=bool,
              help='change the task done state (True or False)')
def update(task_id, owner, summary, done):
    """Modify a task in db with given id with new info."""
    with _tasks_db():
        tasks.update(task_id, Task(summary, owner, done))


@tasks_cli.command(help="list count")
def count():
    """Return number of tasks in db."""
    with _tasks_db():
        c = tasks.count()
        print(c)


@contextmanager
def _tasks_db():
    config = tasks.config.get_config()
    tasks.start_tasks_db(config.db_path, config.db_type)
    yield
    tasks.stop_tasks_db()


if __name__ == '__main__':
    tasks_cli()
