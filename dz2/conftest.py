import pytest


@pytest.fixture(params=["test"])
def fixture_with_params(request):
    return request.param

