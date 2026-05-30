from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Clase base para todos los Page Objects."""

    BASE_URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, path=""):
        self.driver.get(f"{self.BASE_URL}{path}")

    def find(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def find_clickable(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))

    def find_all(self, by, value):
        self.wait.until(EC.presence_of_all_elements_located((by, value)))
        return self.driver.find_elements(by, value)

    def get_text(self, by, value):
        return self.find(by, value).text

    def is_visible(self, by, value):
        try:
            return self.wait.until(EC.visibility_of_element_located((by, value))).is_displayed()
        except Exception:
            return False

    def get_current_url(self):
        return self.driver.current_url
