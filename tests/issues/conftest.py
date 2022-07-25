import pytest

from tests.conftest import v1_maker

issues = v1_maker.make_router('/issues')


@pytest.fixture(scope='session')
def issues_route():
    return issues
