import pytest

from models.users import UserBase, User

from tests.users.conftest import TEST_USER_ID
from tests.conftest import WRONG_PARAMETERS


def test_get_users(users_route):
    response = users_route.get()
    response.assert_status_code([200]).validate(User)


@pytest.mark.parametrize("limit, offset", [
    (1, 1),
    (3, 1)
])
def test_get_users_with_limit_and_offset(users_route, limit, offset):
    response = users_route.set_filters({"limit": limit, "offset": offset}).get()
    response.assert_status_code([200]).validate(User).assert_parameter(
        "limit", limit
    ).assert_parameter("offset", offset)


def test_get_single_player(users_route):
    response = users_route.add_to_path(f'/{TEST_USER_ID}').get()
    response.assert_status_code([200]).validate(User, '')


@pytest.mark.parametrize("user_id", WRONG_PARAMETERS)
def test_get_absent_user(user_id, users_route):
    response = users_route.add_to_path(f'/{user_id}').get()
    response.assert_status_code([404, 422])


def test_create_user(users_route, get_user):
    response = users_route.post(json=get_user.build())
    response.assert_status_code([201]).validate(
        UserBase, response_validation_key=''
    )


@pytest.mark.parametrize("parameter", ["first_name", "company_id"])
def test_creation_with_empty_params(parameter, users_route, get_user):
    user_data = get_user.build()
    user_data[parameter] = None
    response = users_route.post(json=user_data)
    response.assert_status_code([201]).validate(
        UserBase, response_validation_key=''
    )


@pytest.mark.parametrize("parameter", ["first_name"])
def test_creation_without_params(parameter, users_route, get_user):
    user_data = get_user.build()
    del user_data[parameter]
    response = users_route.post(json=user_data)
    response.assert_status_code([201])


@pytest.mark.parametrize('field, parameter', [
    ("company_id", 1),
    ("first_name", 'ETO'),
    ("last_name", 'BAG')
])
def test_updating_user(users_route, create_user, field, parameter):
    user_data = create_user.dict()
    user_data[field] = parameter
    response = users_route.add_to_path(f'/{create_user.user_id}').put(
        json=user_data)
    response.assert_status_code([200]).validate(
        User, response_validation_key=''
    ).assert_parameter(field, parameter)


def test_delete_user(users_route, create_user):
    response = users_route.add_to_path(f'/{create_user.user_id}').delete()
    response.assert_status_code([202])


@pytest.mark.parametrize("wrong_user_id", WRONG_PARAMETERS)
def test_delete_user_by_wrong_id(wrong_user_id, users_route):
    response = users_route.add_to_path(f'/{wrong_user_id}').delete()
    response.assert_status_code([404, 422])
