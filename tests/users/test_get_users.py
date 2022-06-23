import pytest

from models.users import User, UserList


def test_get_users(users_route):
    response = users_route.get()
    response.assert_status_code([200]).validate(User)


@pytest.mark.parametrize("page", [
    1, 10, 30
])
def test_pagination_users(page, users_route):
    response = users_route.set_filters({"page": page}).get()
    response.assert_status_code([200]).assert_parameter(
        'page', page).validate(User)


def test_get_single_player(users_route):
    response = users_route.add_to_path('/2').get()
    response.assert_status_code([200]).validate(User)


def test_get_absent_user(users_route):
    response = users_route.add_to_path('/23').get()
    response.assert_status_code([404])


def test_users_list_structure(users_route):
    response = users_route.get()
    response.assert_status_code([200]).validate(UserList, '')
