import pytest

from tests.conftest import v1_maker

issues = v1_maker.make_router(
    '/issues', default_headers={"hi": "its me", "name": "Mario"}
)


@pytest.fixture(scope='session')
def issues_route():
    return issues
