from pytest import fixture


def pytest_addoption(parser):
    parser.addoption(
        "--name",
        action="store",default="default_value", help="My custom command line argument"
    )

#@fixture()
#def name(request):
#    return request.config.getoption("--name")