"""
Tests de Login - Swag Labs (saucedemo.com)
==========================================
Funcionalidad: Inicio de Sesión
Casos cubiertos:
  TC-L01: Login exitoso con credenciales válidas              [POSITIVO - P1]
  TC-L02: Login con usuario inválido                          [NEGATIVO - P1]
  TC-L03: Login con usuario bloqueado                         [NEGATIVO - P1]
  TC-L04: Login con usuario vacío                             [NEGATIVO - P2]
  TC-L05: Login con password vacío                            [NEGATIVO - P2]
  TC-L06: Login con ambos campos vacíos                       [NEGATIVO - P3]
  TC-L07: Login fallido - FALLA INTENCIONAL para demo reporte [FALLA INTENCIONAL]
"""

import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.constants import (
    VALID_USER, VALID_PASSWORD,
    INVALID_USER, INVALID_PASSWORD,
    LOCKED_USER, EMPTY_STRING,
    INVENTORY_URL,
    ERROR_INVALID_CREDENTIALS, ERROR_LOCKED_USER,
    ERROR_EMPTY_USERNAME, ERROR_EMPTY_PASSWORD,
)


class TestLogin:

    # ── TC-L01: Happy Path ────────────────────────────────────────────────────
    def test_TC_L01_login_exitoso_con_credenciales_validas(self, driver):
        """
        TC-L01 | Login. Al ingresar credenciales válidas, el sistema autentica al usuario.
        Se espera que se redirija al inventario de productos.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, VALID_PASSWORD)

        inventory_page = InventoryPage(driver)
        assert inventory_page.is_loaded(), \
            "El inventario no cargó luego del login exitoso"
        assert INVENTORY_URL in driver.current_url, \
            f"URL esperada: {INVENTORY_URL} | URL obtenida: {driver.current_url}"
        assert inventory_page.get_page_title() == "Products", \
            "El título de la página no es 'Products'"

    # ── TC-L02: Credenciales inválidas ────────────────────────────────────────
    def test_TC_L02_login_con_usuario_invalido(self, driver):
        """
        TC-L02 | Login. Al ingresar usuario incorrecto y password válido,
        el sistema rechaza el acceso. Se espera mensaje de error de credenciales inválidas.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(INVALID_USER, VALID_PASSWORD)

        assert login_page.is_error_displayed(), \
            "No se mostró mensaje de error con usuario inválido"
        assert ERROR_INVALID_CREDENTIALS in login_page.get_error_message(), \
            f"Mensaje de error incorrecto: {login_page.get_error_message()}"

    # ── TC-L03: Usuario bloqueado ─────────────────────────────────────────────
    def test_TC_L03_login_con_usuario_bloqueado(self, driver):
        """
        TC-L03 | Login. Al ingresar con un usuario bloqueado,
        el sistema rechaza el acceso. Se espera mensaje de usuario bloqueado.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(LOCKED_USER, VALID_PASSWORD)

        assert login_page.is_error_displayed(), \
            "No se mostró mensaje de error con usuario bloqueado"
        assert ERROR_LOCKED_USER in login_page.get_error_message(), \
            f"Mensaje de error incorrecto: {login_page.get_error_message()}"

    # ── TC-L04: Username vacío ────────────────────────────────────────────────
    def test_TC_L04_login_con_usuario_vacio(self, driver):
        """
        TC-L04 | Login. Al intentar ingresar sin completar el campo usuario,
        el sistema bloquea el acceso. Se espera mensaje de usuario requerido.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(EMPTY_STRING, VALID_PASSWORD)

        assert login_page.is_error_displayed(), \
            "No se mostró mensaje de error con usuario vacío"
        assert ERROR_EMPTY_USERNAME in login_page.get_error_message(), \
            f"Mensaje de error incorrecto: {login_page.get_error_message()}"

    # ── TC-L05: Password vacío ────────────────────────────────────────────────
    def test_TC_L05_login_con_password_vacio(self, driver):
        """
        TC-L05 | Login. Al intentar ingresar sin completar el campo password,
        el sistema bloquea el acceso. Se espera mensaje de password requerido.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, EMPTY_STRING)

        assert login_page.is_error_displayed(), \
            "No se mostró mensaje de error con password vacío"
        assert ERROR_EMPTY_PASSWORD in login_page.get_error_message(), \
            f"Mensaje de error incorrecto: {login_page.get_error_message()}"

    # ── TC-L06: Ambos campos vacíos ───────────────────────────────────────────
    def test_TC_L06_login_con_ambos_campos_vacios(self, driver):
        """
        TC-L06 | Login. Al intentar ingresar con ambos campos vacíos,
        el sistema bloquea el acceso. Se espera mensaje de usuario requerido.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(EMPTY_STRING, EMPTY_STRING)

        assert login_page.is_error_displayed(), \
            "No se mostró mensaje de error con ambos campos vacíos"
        assert ERROR_EMPTY_USERNAME in login_page.get_error_message(), \
            f"Mensaje de error incorrecto: {login_page.get_error_message()}"

    # ── TC-L07: FALLA INTENCIONAL ─────────────────────────────────────────────
    def test_TC_L07_falla_intencional_para_demo_reporte(self, driver):
        """
        TC-L07 | FALLA INTENCIONAL — Este caso falla intencionalmente para
        demostrar la captura de screenshot en el reporte HTML.
        Login. Al ingresar credenciales válidas, se espera URL incorrecta
        para forzar el fallo y capturar evidencia.
        """
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(VALID_USER, VALID_PASSWORD)

        # Aserción incorrecta intencional — genera fallo + screenshot automático
        assert "checkout" in driver.current_url, \
            "[FALLA INTENCIONAL] Se esperaba URL de checkout pero el usuario " \
            "llegó al inventario. Este caso falla para demostrar el mecanismo " \
            "de captura de screenshots en fallos."
