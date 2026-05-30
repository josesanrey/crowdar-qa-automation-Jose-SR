from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object para la pantalla de Inventario (catálogo de productos)."""

    # ── Locators ─────────────────────────────────────────────────────────────
    PAGE_TITLE          = (By.CSS_SELECTOR, ".title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    INVENTORY_ITEMS     = (By.CSS_SELECTOR, ".inventory_item")
    CART_ICON           = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE          = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def _add_button(self, product_name: str):
        """Retorna el botón 'Add to cart' de un producto por nombre."""
        items = self.find_all(*self.INVENTORY_ITEMS)
        for item in items:
            name_el = item.find_element(By.CSS_SELECTOR, ".inventory_item_name")
            if name_el.text.strip() == product_name:
                return item.find_element(By.CSS_SELECTOR, "button")
        raise ValueError(f"Producto '{product_name}' no encontrado en el inventario.")

    def _remove_button_by_data_test(self, data_test_id: str):
        return self.find_clickable(By.CSS_SELECTOR, f"[data-test='{data_test_id}']")

    def is_loaded(self) -> bool:
        return self.is_visible(*self.INVENTORY_CONTAINER)

    def get_page_title(self) -> str:
        return self.get_text(*self.PAGE_TITLE)

    def add_product_to_cart(self, product_name: str):
        self._add_button(product_name).click()
        return self

    def get_cart_count(self) -> int:
        try:
            return int(self.get_text(*self.CART_BADGE))
        except Exception:
            return 0

    def go_to_cart(self):
        self.find_clickable(*self.CART_ICON).click()

    def get_all_product_names(self) -> list:
        items = self.find_all(*self.INVENTORY_ITEMS)
        return [item.find_element(By.CSS_SELECTOR, ".inventory_item_name").text for item in items]
