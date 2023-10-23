import pytest


def pytest_addoption(parser):
    parser.addoption("--param_file")

@pytest.fixture(scope='session', autouse=True)
def param_file(request):
    return request.config.getoption("--param_file")