# 🧪 Swag Labs — Framework de Automatización QA

**Challenge Automation | Crowdar | José Sanchez Reynoso**

Framework de automatización para [Swag Labs (saucedemo.com)](https://www.saucedemo.com), construido con Python + Selenium WebDriver + Pytest. Cubre las funcionalidades de **Login** y **Carrito de compras**, con soporte multi-browser, reportes HTML y captura automática de screenshots en fallos.

---

## 🛠 Stack

| Herramienta | Versión | Uso |
|---|---|---|
| Python | 3.10+ | Lenguaje base |
| Selenium WebDriver | 4.21 | Automatización de browser |
| Pytest | 8.2 | Framework de testing |
| pytest-html | 4.1 | Reportes HTML |
| webdriver-manager | 4.0 | Gestión automática de drivers |
| Requests | 2.32 | Tests de API REST |

---

## 📁 Estructura del Proyecto

```
eki-automation/
├── pages/                     # Page Objects
│   ├── base_page.py           # Clase base con métodos comunes
│   ├── login_page.py          # Page Object: Login
│   ├── inventory_page.py      # Page Object: Inventario/Productos
│   └── cart_page.py           # Page Object: Carrito
├── tests/                     # Casos de prueba
│   ├── test_login.py          # Tests de inicio de sesión (7 casos)
│   ├── test_cart.py           # Tests de carrito de compras (5 casos)
│   └── test_api_mercadolibre.py # Test de API MercadoLibre
├── utils/
│   └── constants.py           # Constantes y datos de prueba
├── reports/                   # Reportes HTML generados (auto)
├── screenshots/               # Screenshots de fallos (auto)
├── conftest.py                # Fixtures y configuración de Pytest
├── pytest.ini                 # Configuración de Pytest
└── requirements.txt           # Dependencias
```

---

## ⚙️ Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/josesanrey/crowdar-automation-challenge.git
cd crowdar-automation-challenge
```

### 2. Crear entorno virtual (recomendado)
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

> Los drivers de Chrome y Firefox se descargan automáticamente con `webdriver-manager`. No se requiere instalación manual.

---

## ▶️ Ejecución

### Ejecutar todos los tests en Chrome (default)
```bash
pytest
```

### Ejecutar en Firefox
```bash
pytest --browser=firefox
```

### Ejecutar solo tests de Login
```bash
pytest tests/test_login.py
```

### Ejecutar solo tests de Carrito
```bash
pytest tests/test_cart.py
```

### Ejecutar solo tests de API
```bash
pytest tests/test_api_mercadolibre.py
```

### Ejecutar en ambos browsers (Chrome + Firefox)
```bash
pytest --browser=chrome && pytest --browser=firefox --html=reports/report_firefox.html
```

---

## 📊 Reportes

El reporte HTML se genera automáticamente en:
```
reports/report.html
```

Abrirlo en cualquier browser para ver:
- Resumen de ejecución (passed / failed / errors)
- Detalle de cada test con logs
- **Screenshots adjuntos automáticamente en los casos fallidos**

---

## 📸 Screenshots en fallos

Ante cualquier test fallido, se captura automáticamente un screenshot que se guarda en:
```
screenshots/<nombre_test>_<timestamp>.png
```

Los screenshots también se adjuntan inline en el reporte HTML.

---

## 🧪 Casos de Prueba

### Login (7 casos)
| ID | Título | Tipo | Prioridad |
|---|---|---|---|
| TC-L01 | Login exitoso con credenciales válidas | Positivo | P1 |
| TC-L02 | Login con usuario inválido | Negativo | P1 |
| TC-L03 | Login con usuario bloqueado | Negativo | P1 |
| TC-L04 | Login con usuario vacío | Negativo | P1 |
| TC-L05 | Login con password vacío | Negativo | P1 |
| TC-L06 | Login con ambos campos vacíos | Negativo | P2 |
| TC-L07 | **Falla intencional** — demo de screenshot en reporte | Intencional | — |

### Carrito (5 casos)
| ID | Título | Tipo | Prioridad |
|---|---|---|---|
| TC-C01 | Agregar un producto al carrito | Positivo | P1 |
| TC-C02 | Agregar múltiples productos al carrito | Positivo | P1 |
| TC-C03 | Eliminar un producto del carrito | Positivo | P2 |
| TC-C04 | Carrito persiste al navegar | Positivo | P2 |
| TC-C05 | Carrito vacío no muestra badge | Negativo | P2 |

### API (1 caso)
| ID | Título | Tipo |
|---|---|---|
| TC-API-01 | GET /menu/departments retorna lista válida | API |

---

## 👤 Autor

**José Sanchez Reynoso** — QA Lead  
[linkedin.com/in/josesanrey](https://linkedin.com/in/josesanrey)
