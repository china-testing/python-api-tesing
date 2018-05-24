Changelog
=========

-----------------------------------------------------------------

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


---------------------------------------------------

0.1.0
-----

Changes:
~~~~~~~~

- Initial version.

