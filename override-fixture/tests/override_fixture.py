import pytest


@pytest.fixture()
def foo():
    return 'boo'


@pytest.fixture()
def bar():
    return 'far'


def test_fixture(foobar):
    assert foobar == 'boofar'
