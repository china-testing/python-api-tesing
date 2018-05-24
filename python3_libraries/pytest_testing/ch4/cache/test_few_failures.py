"""Demonstrate -lf and -ff with failing tests."""

import pytest
from pytest import approx


testdata = [
    # x, y, expected
    (1.01, 2.01, 3.02),
    (1e25, 1e23, 1.1e25),
    (1.23, 3.21, 4.44),
    (0.1, 0.2, 0.3),
    (1e25, 1e24, 1.1e25)
]


@pytest.mark.parametrize("x,y,expected", testdata)
def test_a(x, y, expected):
    """Demo approx()."""
    sum_ = x + y
    assert sum_ == approx(expected)
