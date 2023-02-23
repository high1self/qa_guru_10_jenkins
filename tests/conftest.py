import pytest
from selene.support.shared import browser
from demoqa_tests.utils import attach


@pytest.fixture(scope="session", autouse=True)
def app():
    # browser.config.browser_name = 'firefox'
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()