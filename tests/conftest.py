from datetime import datetime
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from utils.config_parser import ConfigParserIni, AllureEnvironmentParser


# Reads parameters from pytest command line
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser that the automation will run in")


@pytest.fixture(scope="session")
# Instantiates ini file parser object
def prep_properties():
    config_reader = ConfigParserIni("props.ini")
    return config_reader


@pytest.fixture(autouse=True)
# Fetch browser kind and base URL, then write a dictionary of key-value pairs into allure's environment.properties file
def write_allure_environment(prep_properties, request):
    yield
    env_parser = AllureEnvironmentParser("environment.properties")
    env_parser.write_to_allure_env({"browser": request.config.option.browser, "base_url": prep_properties.config_section_dict("AUT")["base_url"]})


@pytest.fixture(autouse=True)
# Performs setup and tear down
def create_driver(prep_properties, request):
    global driver
    browser = request.config.option.browser
    base_url = prep_properties.config_section_dict("AUT")["base_url"]

    if browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser == "remote":
        capabilities = {
            'browserName': 'firefox',
            'javascriptEnabled': True
        }
        driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", desired_capabilities=capabilities)
    elif browser == "chrome_headless":
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get(base_url)

    yield driver  # Provide the driver to tests

    # Close the browser after the test
    driver.quit()


@pytest.fixture(autouse=True)
def pages(create_driver):  #
    login_page = LoginPage(create_driver)  #
    return {"login_page": login_page}


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set a report attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)