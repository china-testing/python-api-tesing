import pytest
import os


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print('Point.__init__()')

    def __repr__(self):
        return 'Point({},{})'.format(self.x, self.y)

    def __str__(self):
        return '({},{})'.format(self.x, self.y)


@pytest.fixture(name='a_point', scope='module')
def point_fixture():
    return Point(1, 2)


def test_point_repr(a_point, monkeypatch):
    monkeypatch.setattr(a_point, 'x', 10)
    assert repr(a_point) == 'Point(10,2)'


def test_point_str(a_point, monkeypatch):
    monkeypatch.setattr(a_point, 'y', 20)
    assert str(a_point) == '(1,20)'


def test_point_missing_x(a_point, monkeypatch):
    monkeypatch.delattr(a_point, 'x')
    with pytest.raises(AttributeError):
        str(a_point)


def test_env(monkeypatch):
    monkeypatch.setenv('HOME', '/Users/foo')
    assert os.environ['HOME'] == '/Users/foo'


def test_prepend(monkeypatch):
    monkeypatch.setenv('PATH', '/Users/okken/bin', ':')
    assert os.environ['PATH'].startswith('/Users/okken/bin')
