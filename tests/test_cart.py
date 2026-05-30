"""
Tests de Carrito - Swag Labs (saucedemo.com)
============================================
Funcionalidad: Agregado de productos al carrito de compras
Casos cubiertos:
  TC-C01: Agregar un producto al carrito desde el inventario   [POSITIVO - P1]
  TC-C02: Agregar múltiples productos al carrito               [POSITIVO - P1]
  TC-C03: Eliminar un producto del carrito                     [POSITIVO - P2]
  TC-C04: Verificar que el carrito persiste al navegar         [POSITIVO - P2]
  TC-C05: Carrito vacío no muestra badge en el ícono           [NEGATIVO - P2]
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.constants import (
    VALID_USER, VALID_PASSWORD,
    PRODUCT_BACKPACK, PRODUCT_BIKE_LIGHT, PRODUCT_BOLT_TSHIRT,
    CART_URL,
)


@pytest.fixture(autouse=True)
def login(driver):
    """Fixture: hace login antes de cada test de carrito."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USER, VALID_PASSWORD)
    yield


class TestCart:

    # ── TC-C01: Agregar un producto ───────────────────────────────────────────
    def test_TC_C01_agregar_un_producto_al_carrito(self, driver):
        """
        TC-C01 | Carrito. Al agregar un producto desde el inventario,
        el sistema lo registra en el carrito. Se espera que el badge del
        ícono muestre 1 y el producto aparezca en la vista del carrito.
        """
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(PRODUCT_BACKPACK)

        assert inventory.get_cart_count() == 1, \
            f"Badge esperado: 1 | Badge obtenido: {inventory.get_cart_count()}"

        inventory.go_to_cart()
        cart = CartPage(driver)

        assert cart.is_loaded(), "La página del carrito no cargó correctamente"
        assert PRODUCT_BACKPACK in cart.get_cart_items(), \
            f"'{PRODUCT_BACKPACK}' no aparece en el carrito"

    # ── TC-C02: Agregar múltiples productos ───────────────────────────────────
    def test_TC_C02_agregar_multiples_productos_al_carrito(self, driver):
        """
        TC-C02 | Carrito. Al agregar múltiples productos desde el inventario,
        el sistema los registra todos. Se espera que el badge muestre la
        cantidad correcta y todos los productos aparezcan en el carrito.
        """
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(PRODUCT_BACKPACK)
        inventory.add_product_to_cart(PRODUCT_BIKE_LIGHT)
        inventory.add_product_to_cart(PRODUCT_BOLT_TSHIRT)

        assert inventory.get_cart_count() == 3, \
            f"Badge esperado: 3 | Badge obtenido: {inventory.get_cart_count()}"

        inventory.go_to_cart()
        cart = CartPage(driver)
        cart_items = cart.get_cart_items()

        assert PRODUCT_BACKPACK in cart_items, \
            f"'{PRODUCT_BACKPACK}' no aparece en el carrito"
        assert PRODUCT_BIKE_LIGHT in cart_items, \
            f"'{PRODUCT_BIKE_LIGHT}' no aparece en el carrito"
        assert PRODUCT_BOLT_TSHIRT in cart_items, \
            f"'{PRODUCT_BOLT_TSHIRT}' no aparece en el carrito"
        assert cart.get_cart_item_count() == 3, \
            f"Items en carrito esperados: 3 | Obtenidos: {cart.get_cart_item_count()}"

    # ── TC-C03: Eliminar un producto del carrito ──────────────────────────────
    def test_TC_C03_eliminar_producto_del_carrito(self, driver):
        """
        TC-C03 | Carrito. Al eliminar un producto desde la vista del carrito,
        el sistema lo remueve correctamente. Se espera que el producto
        desaparezca del carrito y el badge se actualice.
        """
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(PRODUCT_BACKPACK)
        inventory.add_product_to_cart(PRODUCT_BIKE_LIGHT)
        inventory.go_to_cart()

        cart = CartPage(driver)
        assert cart.get_cart_item_count() == 2, "El carrito debería tener 2 items antes de eliminar"

        cart.remove_item(PRODUCT_BACKPACK)

        remaining = cart.get_cart_items()
        assert PRODUCT_BACKPACK not in remaining, \
            f"'{PRODUCT_BACKPACK}' debería haber sido eliminado del carrito"
        assert PRODUCT_BIKE_LIGHT in remaining, \
            f"'{PRODUCT_BIKE_LIGHT}' no debería haber sido eliminado"

    # ── TC-C04: Persistencia del carrito ──────────────────────────────────────
    def test_TC_C04_carrito_persiste_al_navegar(self, driver):
        """
        TC-C04 | Carrito. Al agregar un producto y navegar de vuelta al inventario,
        el carrito mantiene el item agregado. Se espera que el badge
        conserve el valor y el producto siga en el carrito.
        """
        inventory = InventoryPage(driver)
        inventory.add_product_to_cart(PRODUCT_BACKPACK)

        assert inventory.get_cart_count() == 1

        inventory.go_to_cart()
        cart = CartPage(driver)
        cart.continue_shopping()

        inventory_back = InventoryPage(driver)
        assert inventory_back.get_cart_count() == 1, \
            "El badge del carrito no persistió luego de navegar de vuelta al inventario"

    # ── TC-C05: Carrito vacío sin badge ───────────────────────────────────────
    def test_TC_C05_carrito_vacio_no_muestra_badge(self, driver):
        """
        TC-C05 | Carrito. Al acceder al inventario sin agregar productos,
        el ícono del carrito no muestra badge de cantidad.
        Se espera que el badge sea 0 (no visible).
        """
        inventory = InventoryPage(driver)

        assert inventory.get_cart_count() == 0, \
            f"El badge del carrito debería ser 0 pero muestra: {inventory.get_cart_count()}"
