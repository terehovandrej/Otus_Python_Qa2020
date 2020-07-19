import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        wd = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        wd = webdriver.Firefox(options=options)
    elif browser_name == "ie":
        wd = webdriver.Ie()
        wd.maximize_window()
    else:
        raise pytest.UsageError("browser should be chrome, firefox or IE")
    yield wd
    wd.quit()


@pytest.fixture(scope="function")
def base_url(request):
    return request.config.getoption("--url")


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help="Choose browser: chrome, firefox or IE")
    parser.addoption(
        '--url',
        action='store',
        default='http://localhost/',
        help='This is base url'
    )
