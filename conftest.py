import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

SCREENSHOTS_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Browser: chrome | firefox")

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser").lower()
    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        drv = webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        drv = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser '{browser}' no soportado.")
    drv.implicitly_wait(10)
    yield drv
    drv.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)
            driver.save_screenshot(filepath)
            try:
                from pytest_html import extras
                report.extra = getattr(report, "extra", [])
                report.extra.append(extras.image(filepath))
            except Exception:
                pass
            print(f"\n📸 Screenshot: {filepath}")
