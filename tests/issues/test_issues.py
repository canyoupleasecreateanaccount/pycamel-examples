from models.companies import Company
from models.users import User


def test_getting_companies_with_filter(issues_route):
    response = issues_route.add_to_path('/companies').set_filters({
        "status": "ACTIVE"}).get()
    response.assert_status_code([200]).validate(Company).assert_parameter(
        "company_status", "ACTIVE"
    )


def test_getting_companies_with_timeout(issues_route):
    issues_route.add_to_path('/companies/1').get(timeout=2)


def test_creating_user(issues_route):
    last_name = "Ivan"
    response = issues_route.add_to_path('/users').post(
        json={"last_name": last_name})
    response.assert_status_code([201]).validate(User, '').assert_parameter(
        "last_name", last_name
    )
