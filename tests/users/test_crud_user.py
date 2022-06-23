import pytest

from models.users import UserCreate, UserUpdate


def test_create_user(users_route, get_user):
    response = users_route.post(json=get_user.build())
    response.assert_status_code([201]).validate(
        UserCreate,
        response_validation_key=''
    )


@pytest.mark.parametrize("parameter", ["name", "job"])
def test_creation_with_empty_params(parameter, users_route, get_user):
    user_data = get_user.build()
    user_data[parameter] = ''
    response = users_route.post(json=user_data)
    response.assert_status_code([201]).validate(
        UserCreate, response_validation_key=''
    )


@pytest.mark.parametrize("parameter", ["name", "job"])
def test_creation_without_params(parameter, users_route, get_user):
    user_data = get_user.build()
    del user_data[parameter]
    response = users_route.post(json=user_data)
    response.assert_status_code([201])


def test_updating_user(users_route, get_user):
    user = get_user.build()
    response = users_route.add_to_path('/2').put(json=user)
    response.assert_status_code([200]).validate(
        UserUpdate, response_validation_key=''
    )


@pytest.mark.parametrize("parameter", ["name", "job"])
def test_updating_user_partially(parameter, get_user, users_route):
    """
    According to convention, as I know, after patch executing, BE should
    include into response all data about updated object.

    So, let it be, this case will have failed status for example ^_^
    """
    user = get_user.build()
    response = users_route.add_to_path('/2').patch(
        json={parameter: user[parameter]}
    )
    response.assert_status_code([200]).validate(
        UserUpdate, response_validation_key=''
    )


def test_delete_user(users_route):
    response = users_route.add_to_path('/2').delete()
    response.assert_status_code([204])


def test_delay_response(users_route):
    """
    Sorry, it is second example of failing test.
    As you can see, you can pass any default params into request methods (.get())
    that described in default requests library.
    """
    response = users_route.set_filters({"delay": 3}).get(timeout=1)
    response.assert_status_code([200])
