import pytest

from tests.conftest import v1_maker

from generators.user import UserGenerator

users = v1_maker.make_router('/users')

USER = UserGenerator()


@pytest.fixture(scope='session')
def users_route():
    return users


@pytest.fixture(scope='session')
def get_user():
    return USER


