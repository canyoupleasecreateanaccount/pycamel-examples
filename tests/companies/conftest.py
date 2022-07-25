import pytest

from tests.conftest import v1_maker

TEST_COMPANY_ID = 1

companies = v1_maker.make_router('/companies')


@pytest.fixture(scope='session')
def companies_route():
    return companies
