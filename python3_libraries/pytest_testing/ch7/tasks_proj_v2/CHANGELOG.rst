Changelog
=========
----------------------------------------------------

0.1.1 (ch7/tasks_proj_2)
------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- All of what was here: ch6/b/tasks_proj/tests
- tasks_proj/tox.ini added to demonstrate tox
- tests/pytest.ini contents moved to tasks_proj/tox.ini
- tests/unit/test_cli.py added to demonstrate mock

Fixes in src: 
~~~~~~~~~~~~~

- src/tasks/api.py 
    - Fix problem where tasks.add() didn't raise an exception if ``done`` param passed in wasn't a bool. 
- src/tasks/tasksdb_pymongo.py 
    - Fix problem where tasks.add() was returning an object as an id instead of an integer

----------------------------------------------------

0.1.0 (ch6/b/tasks_proj)
------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- add content to pytest.ini:
    - declare markers (smoke, get)
    - set some of my favorite options as defaults with addopts

Known Issues: (no changes)
~~~~~~~~~~~~~~~~~~~~~~~~~~

- tasks.add() should raise an exception if ``done`` param passed in isn't a bool. It currently doesn't.
- MongoDB still doesn't work.

----------------------------------------------------

0.1.0 (ch6/a/tasks_proj)
------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - remove ``--nice`` option
    - it's available as a plugin in ch5/pytest-nice if we want it.

Known Issues: (no changes)
~~~~~~~~~~~~~~~~~~~~~~~~~~

- tasks.add() should raise an exception if ``done`` param passed in isn't a bool. It currently doesn't.
- MongoDB still doesn't work.

----------------------------------------------------

0.1.0 (ch5/c/tasks_proj/tests)
------------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - add a ``--nice`` option to pytest for the:
        - test header
        - turning failure into opportunity

Known Issues: (no changes)
~~~~~~~~~~~~~~~~~~~~~~~~~~

- tasks.add() should raise an exception if ``done`` param passed in isn't a bool. It currently doesn't.
- MongoDB still doesn't work.
- Maybe we should have been working on fixing bugs instead playing with nice options. Just saying.

----------------------------------------------------

0.1.0 (ch5/b/tasks_proj/tests)
------------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - add a test header
    - turn failure into opportunity

Known Issues: (no changes)
~~~~~~~~~~~~~~~~~~~~~~~~~~

- tasks.add() should raise an exception if ``done`` param passed in isn't a bool. It currently doesn't.
- MongoDB still doesn't work.

----------------------------------------------------

0.1.0 (ch5/a/tasks_proj/tests)
------------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - put ``tasks_db_session`` back to just testing TinyDB. The fix for the MongoDB is in ch7/tasks_proj_v2, if you're curious. But for now, testing with TinyDB is sufficient.

- tests/func/test_api_exceptions.py:
    - add a couple more tests. One that demonstrates a failure. 

Known Issues:
~~~~~~~~~~~~~

- tasks.add() allows a ``done`` param to be a string. Shouldn't.
- MongoDB still doesn't work.


----------------------------------------------------

0.1.0 (ch3/c/tasks_proj/tests)
------------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - parametrize ``tasks_db_session`` to test both TinyDB and MongoDB.

Known Issues:
~~~~~~~~~~~~~

- Lots of tests fail.
    - possibly due to some problem with task_id with the MongoDB version

----------------------------------------------------

0.1.0 (ch3/b/tasks_proj/tests)
------------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- modify tests/conftest.py:
    - Create a session scope fixture ``tasks_db_session``
      that connects to db.
    - Have ``tasks_db`` fixture use ``tasks_db_session`` and 
      just clean out db between tests.

- add tests/func/test_add_variety2.py
    - demonstrate paramterized fixtures


----------------------------------------------------

0.1.0 (ch3/a/tasks_proj/tests)
------------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- add tests/conftest.py with fixtures:
    - tasks_just_a_few : 3 tasks in a tuple
    - tasks_mult_per_owner : 9 tasks with 3 owners
    - tasks_db : connection to db, using TinyDB
    - db_with_3_tasks : db prefilled with 3 tasks
    - db_with_multi_per_owner : db prefilled with 9 tasks

- modify to use fixtures:
    - test_add.py
    - test_add_variety.py
    - test_api_exceptions.py
    - test_unique_id.py

- remove tests/unit/test_task_fail.py  
    - it was just to demo failures

- remove tests/func/test_unique_id_1.py
- remove tests/func/test_unique_id_2.py
- remove tests/func/test_unique_id_3.py 
- remove tests/func/test_unique_id_4.py
- add tests/func/test_unique_id.py
    - just need one unique_id test.


----------------------------------------------------

0.1.0 (ch2/tasks_proj/tests)
----------------------------

Changes to tests:
~~~~~~~~~~~~~~~~~

- added tests/unit/test_Task.py 
    - a few tests to demonstrate running tests

- added tests/unit/test_Task_fail.py 
    - demonstrate test failure

- added tests/func/test_api_exceptions.py
    - testing for expected exceptions

- added tests/func/test_add.py
    - testing ``tasks.add()``
    - demonstrate user defined markers 

- added tests/func/test_unique_id_1.py
    - initial tests for ``tasks.unique_id()``.

- added tests/func/test_unique_id_2.py
    - demonstrate ``@pytest.mark.skip()``.

- added tests/func/test_unique_id_3.py : 
    - demonstrate ``@pytest.mark.skipif()``.

- added tests/func/test_unique_id_4.py
    - demonstrate ``@pytest.mark.xfail()``.

- added tests/func/test_add_variety.py
    - demonstrate ``@pytest.mark.parametrize`` on functions and classes.


----------------------------------------------------

0.1.0
-----

Changes:
~~~~~~~~

- Initial version.

