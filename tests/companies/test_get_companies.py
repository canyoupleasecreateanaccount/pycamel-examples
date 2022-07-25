import pytest

from models.companies import Company, CompanyStatuses
from models.project import Meta

from tests.companies.conftest import TEST_COMPANY_ID
from tests.conftest import WRONG_PARAMETERS


def test_get_list_of_companies(companies_route):
    response = companies_route.get()
    response.assert_status_code([200]).validate(Company)


@pytest.mark.parametrize("status", CompanyStatuses.list())
def test_getting_list_with_filter(companies_route, status):
    response = companies_route.set_filters({"status": status}).get()
    response.assert_status_code([200]).validate(Company).assert_parameter(
        "status", status
    )


@pytest.mark.parametrize("limit, offset", [
    (1, 1),
    (3, 1)
])
def test_limit_and_offset_filtering(limit, offset, companies_route):
    response = companies_route.set_filters(
        {"limit": limit, "offset": offset}).get()
    response.assert_status_code([200]).validate(Meta, 'meta').assert_parameter(
        "limit", limit).assert_parameter("offset", offset)


def test_getting_company_by_id(companies_route):
    response = companies_route.add_to_path(f"/{TEST_COMPANY_ID}").get()
    response.assert_status_code([200]).validate(Company, '').assert_parameter(
        "company_id", TEST_COMPANY_ID
    )


@pytest.mark.parametrize("company_id", WRONG_PARAMETERS)
def test_getting_company_id_with_invalid_values(companies_route, company_id):
    response = companies_route.add_to_path(f"/{company_id}").get()
    response.assert_status_code([404, 422])
