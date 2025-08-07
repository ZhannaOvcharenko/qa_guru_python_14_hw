import os
import allure
import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from utils import attach


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


selenoid_login = os.getenv("SELENOID_LOGIN")
selenoid_pass = os.getenv("SELENOID_PASS")
selenoid_url = os.getenv("SELENOID_URL")


@pytest.fixture(scope="function", autouse=True)
def setup_browser():
    options = Options()
    options.add_argument("--incognito")

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        },
        "goog:loggingPrefs": {
            "browser": "ALL",
            "driver": "ALL"
        }
    }
    options.capabilities.update(capabilities)
    options.set_capability("selenoid:options", capabilities["selenoid:options"])
    options.set_capability("goog:loggingPrefs", capabilities["goog:loggingPrefs"])

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.timeout = 20
    browser.config.base_url = "https://www.ebay.com"
    browser.driver.maximize_window()
    browser.driver.delete_all_cookies()

    with allure.step("Open eBay main page"):
        browser.open('/')

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
