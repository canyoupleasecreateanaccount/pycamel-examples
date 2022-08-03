import pytest

from tests.conftest import v1_maker


companies = v1_maker.make_router('/companies')
TEST_COMPANY_ID = 1


@pytest.fixture(scope='session')
def companies_route():
    return companies
