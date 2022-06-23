import pytest

from tests.conftest import v1_maker

resource = v1_maker.make_router('/unknown')


@pytest.fixture(scope='session')
def resource_route():
    return resource
