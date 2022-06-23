import pytest

from models.resources import Resource, ResourceList


def test_get_list_resources(resource_route):
    response = resource_route.get()
    response.assert_status_code([200]).validate(Resource)


@pytest.mark.parametrize("page", [
    1, 10, 30
])
def test_pagination_resource(page, resource_route):
    response = resource_route.set_filters({"page": page}).get()
    response.assert_status_code([200]).assert_parameter(
        'page', page).validate(Resource)


def test_get_single_resource(resource_route):
    response = resource_route.add_to_path('/2').get()
    response.assert_status_code([200]).validate(Resource)


def test_get_absent_resource_by_id(resource_route):
    response = resource_route.add_to_path('/23').get()
    response.assert_status_code([404])


def test_resource_response_structure(resource_route):
    response = resource_route.get()
    response.assert_status_code([200]).validate(ResourceList, '')
