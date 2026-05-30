from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    """Page Object para la pantalla del carrito de compras."""

    # ── Locators ─────────────────────────────────────────────────────────────
    PAGE_TITLE      = (By.CSS_SELECTOR, ".title")
    CART_ITEMS      = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAMES      = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_BUTTONS  = (By.CSS_SELECTOR, "[data-test^='remove-']")
    CONTINUE_BTN    = (By.ID, "continue-shopping")
    CHECKOUT_BTN    = (By.ID, "checkout")

    def is_loaded(self) -> bool:
        return self.is_visible(*self.PAGE_TITLE) and "cart" in self.get_current_url()

    def get_page_title(self) -> str:
        return self.get_text(*self.PAGE_TITLE)

    def get_cart_items(self) -> list:
        try:
            items = self.find_all(*self.ITEM_NAMES)
            return [item.text for item in items]
        except Exception:
            return []

    def get_cart_item_count(self) -> int:
        return len(self.get_cart_items())

    def remove_item(self, product_name: str):
        items = self.find_all(*self.CART_ITEMS)
        for item in items:
            name_el = item.find_element(By.CSS_SELECTOR, ".inventory_item_name")
            if name_el.text.strip() == product_name:
                item.find_element(By.CSS_SELECTOR, "button").click()
                return self
        raise ValueError(f"Producto '{product_name}' no encontrado en el carrito.")

    def is_cart_empty(self) -> bool:
        return self.get_cart_item_count() == 0

    def continue_shopping(self):
        self.find_clickable(*self.CONTINUE_BTN).click()

    def proceed_to_checkout(self):
        self.find_clickable(*self.CHECKOUT_BTN).click()
