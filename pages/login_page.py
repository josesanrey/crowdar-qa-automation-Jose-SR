from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Page Object para la pantalla de Login de Swag Labs."""

    # ── Locators ─────────────────────────────────────────────────────────────
    USERNAME_INPUT    = (By.ID, "user-name")
    PASSWORD_INPUT    = (By.ID, "password")
    LOGIN_BUTTON      = (By.ID, "login-button")
    ERROR_MESSAGE     = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_BUTTON      = (By.CSS_SELECTOR, ".error-button")

    def open(self):
        self.navigate_to("/")
        return self

    def enter_username(self, username: str):
        field = self.find_clickable(*self.USERNAME_INPUT)
        field.clear()
        field.send_keys(username)
        return self

    def enter_password(self, password: str):
        field = self.find_clickable(*self.PASSWORD_INPUT)
        field.clear()
        field.send_keys(password)
        return self

    def click_login(self):
        self.find_clickable(*self.LOGIN_BUTTON).click()
        return self

    def login(self, username: str, password: str):
        """Flujo completo de login."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self) -> str:
        return self.get_text(*self.ERROR_MESSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(*self.ERROR_MESSAGE)

    def is_login_page(self) -> bool:
        return "/index.html" in self.get_current_url() or \
               self.get_current_url().endswith("saucedemo.com/")
