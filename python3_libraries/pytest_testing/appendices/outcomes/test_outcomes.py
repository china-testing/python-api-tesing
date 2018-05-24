import pytest


def test_pass():
    assert 1 == 1


def test_fail():
    assert 1 == 2


@pytest.mark.xfail()
def test_xfail():
    assert 1 == 2


@pytest.mark.xfail()
def test_xpass():
    assert 1 == 1


@pytest.mark.skip()
def test_skip():
    pass


@pytest.fixture()
def flaky_fixture():
    assert 1 == 2


def test_error(flaky_fixture):
    pass
