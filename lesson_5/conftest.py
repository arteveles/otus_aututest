import pytest
import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions, FirefoxOptions
from lesson_5.data_storage import CHROMEDRIVER_PATH, FIREFOX_PATH, OPERA_PATH


def pytest_addoption(parser):
    """
    Выбор браузера. По умолчанию, если не передан аргумент в командную строку - запустится FireFox
    """
    parser.addoption(
        "--browser", default="firefox", help="firefox browser"
    )
    parser.addoption(
        "--drivers", default=os.path.expanduser("~/dev/driver/")
    )
    """
    Отработка тестов без открытия окна браузера
    """
    parser.addoption(
        "--headless", action="store_true"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.headless = True
        _driver = webdriver.Firefox(executable_path=os.path.expanduser(FIREFOX_PATH), options=options)
    elif browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.headless = True
        _driver = webdriver.Chrome(executable_path=os.path.expanduser(CHROMEDRIVER_PATH), options=options)
    elif browser_name == "opera":
        _driver = webdriver.Opera(executable_path=os.path.expanduser(OPERA_PATH))
    else:
        raise ValueError(f"Browser {browser_name} is not supported")

    _driver.maximize_window()

    yield _driver

    _driver.close()
