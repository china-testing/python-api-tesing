Changelog
=========

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


------------------------------------------------------

0.1.0
-----

Changes:
~~~~~~~~

- Initial version.

