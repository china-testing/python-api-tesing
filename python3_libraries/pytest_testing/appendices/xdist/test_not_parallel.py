import pytest
import time


@pytest.fixture(scope='function')
def some_resource():
    x = []
    return x


def test_1(some_resource):
    time.sleep(1)


def test_2(some_resource):
    time.sleep(1)


def test_3(some_resource):
    time.sleep(1)


def test_4(some_resource):
    time.sleep(1)
