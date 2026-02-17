import pytest
import os
from datetime import datetime

import pytest
from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name

            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)

            print(f"\n📸 Screenshot salva em: {screenshot_path}")