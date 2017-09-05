import pytest


@pytest.fixture()
def foo():
    return 'foo'


@pytest.fixture()
def bar():
    return 'bar'


@pytest.fixture()
def foobar(foo, bar):
    return foo + bar
