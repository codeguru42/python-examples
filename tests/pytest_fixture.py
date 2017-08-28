import pytest


@pytest.fixture()
def foo():
    return 'foo'


@pytest.fixture()
def bar():
    return 'bar'


@pytest.fixture()
def baz():
    return 'baz'


@pytest.fixture()
def foobar(foo, bar):
    return foo + bar


@pytest.fixture()
def foobaz(foo, baz):
    return foo + baz


def test(foobar, foobaz):
    print('test')
    print(foobar)
    print(foobaz)
