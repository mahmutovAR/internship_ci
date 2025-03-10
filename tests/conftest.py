from os import getenv

import allure
import pytest
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService

pytest_plugins = 'tests.fixtures'


load_dotenv()


@pytest.fixture(scope="function")
def browser(request):
    # options = Options()
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument('--disable-dev-shm-usage')
    # # service = Service(ChromeDriverManager().install())
    # chrome_driver_path = getenv('CHROME_DRIVER_PATH')
    # service = Service(chrome_driver_path)
    # driver = webdriver.Chrome(service=service, options=options)
    # driver.set_window_size(1920, 1080)
    # yield driver
    # driver.quit()

    options = EdgeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    edge_driver_path = getenv('MSEDGE_DRIVER_PATH')
    driver = webdriver.Edge(service=EdgeService(edge_driver_path), options=options)


    # options = FirefoxOptions()
    # options.add_argument("-headless")
    # options.add_argument("--no-sandbox")
    # gecko_driver_path = getenv('GECKO_DRIVER_PATH')
    # driver = webdriver.Firefox(service=FirefoxService(gecko_driver_path), options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--grid", action="store_true", default=False)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        driver = item.funcargs.get('browser')
        if driver:
            with allure.step('Скриншот упавшего теста'):
                allure.attach(driver.get_screenshot_as_png(),
                              name='Test failure screenshot',
                              attachment_type=AttachmentType.PNG)
