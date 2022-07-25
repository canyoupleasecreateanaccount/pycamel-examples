import pytest

from generators.user import UserGenerator

from models.users import User

from tests.conftest import v1_maker


USER = UserGenerator()
TEST_USER_ID = 1

users = v1_maker.make_router('/users')


@pytest.fixture(scope='session')
def users_route():
    return users


@pytest.fixture(scope='session')
def get_user():
    return USER


@pytest.fixture
def create_user(get_user, users_route):
    response = users_route.post(json=get_user.build())
    user = response.assert_status_code([201]).validate(
        User, '').get_validated_objects()[0] # TODO Issue will be fixed in next release
    yield user
    users_route.add_to_path(f'/{user.user_id}').delete()
