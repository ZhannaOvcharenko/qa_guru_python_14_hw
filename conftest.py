import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from utils import attach
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")
    base_url = os.getenv("BASE_URL", "https://www.ebay.com")

    if not all([selenoid_login, selenoid_pass, selenoid_url]):
        raise ValueError(
            "Не заданы переменные SELENOID_LOGIN, SELENOID_PASS или SELENOID_URL.\n"
            "Убедитесь, что .env файл существует или переменные окружения заданы в Jenkins / CI."
        )

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "screenResolution": "1920x1080x24"
        }
    }

    options.capabilities.update(capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = base_url
    browser.driver.maximize_window()
    browser.config.timeout = 10

    yield

    session_id = driver.session_id

    attach.add_screenshot()
    attach.add_logs()
    attach.add_html()
    attach.add_video(session_id)

    browser.quit()