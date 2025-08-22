# XMLtoExcelPro

<div align="center">

<img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
<img src="https://img.shields.io/github/stars/jfGalvan/XMLtoExcelPro?style=for-the-badge" alt="GitHub Stars">
<img src="https://img.shields.io/github/forks/jfGalvan/XMLtoExcelPro?style=for-the-badge" alt="GitHub Forks">

**🚀 Convierte archivos XML a Excel de forma rápida, precisa y automatizada**

*La herramienta definitiva para transformar tus datos XML en hojas de cálculo Excel profesionales*

[📚 Documentación](#-tabla-de-contenidos) • [🔥 Inicio Rápido](#-inicio-rápido) • [💻 Ejemplos](#-ejemplos-de-uso) • [🤝 Contribuir](#-contribuir) • [🐛 Reportar Bug](https://github.com/jfGalvan/XMLtoExcelPro/issues)

</div>

---

## 📋 Tabla de Contenidos

- [✨ Características](#-características)
- [🎯 ¿Por qué XMLtoExcelPro?](#-por-qué-xmltoexcelpro)
- [⚡ Inicio Rápido](#-inicio-rápido)
- [📦 Instalación Detallada](#-instalación-detallada)
- [🖥️ Modos de Uso](#️-modos-de-uso)
- [💻 Ejemplos de Uso](#-ejemplos-de-uso)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Configuración Avanzada](#️-configuración-avanzada)
- [🧪 Testing](#-testing)
- [🤝 Contribuir](#-contribuir)
- [🐛 Solución de Problemas](#-solución-de-problemas)
- [📄 Licencia](#-licencia)

---

## ✨ Características

### 🚀 **Funcionalidades Core**
- **Conversión XML → Excel**: Transforma archivos XML complejos a formato .xlsx
- **Doble Interfaz**: GUI intuitiva y CLI potente para diferentes necesidades
- **Procesamiento Inteligente**: Detecta automáticamente la estructura XML y optimiza la conversión
- **Soporte Multi-archivo**: Procesa múltiples archivos XML en modo batch
- **Preservación de Datos**: Mantiene tipos de datos, jerarquías y relaciones

### 🛠️ **Características Técnicas**
- **Manejo de XML Complejo**: Soporta namespaces, atributos y estructuras anidadas
- **Optimización de Memoria**: Procesamiento eficiente de archivos grandes (100MB+)
- **Validación de Datos**: Verificación automática de integridad antes y después de la conversión
- **Reportes Detallados**: Logs completos del proceso de conversión
- **Configuración Flexible**: Múltiples opciones de personalización

### 🎨 **Experiencia de Usuario**
- **Interfaz Gráfica Moderna**: UI limpia y fácil de usar con drag & drop
- **Progreso en Tiempo Real**: Barra de progreso y estadísticas de conversión
- **Vista Previa**: Previsualización de datos antes de la conversión final
- **Exportación Personalizable**: Control sobre formato de salida Excel

---

## 🎯 ¿Por qué XMLtoExcelPro?

<table>
<tr>
<td width="50%">

### 🔥 **Problemas que Resuelve**
- ❌ Archivos XML difíciles de leer y analizar
- ❌ Conversiones manuales lentas y propensas a errores  
- ❌ Herramientas complejas que requieren conocimiento técnico
- ❌ Pérdida de estructura de datos durante conversión
- ❌ Procesamiento lento de archivos grandes

</td>
<td width="50%">

### ✅ **Soluciones que Ofrece**
- ✅ Conversión automática en segundos
- ✅ Interfaz intuitiva para cualquier usuario
- ✅ Preservación completa de estructura de datos
- ✅ Procesamiento optimizado para archivos grandes
- ✅ Resultados consistentes y confiables

</td>
</tr>
</table>

### 📊 **Casos de Uso Perfectos**
- **📈 Análisis de Datos**: Científicos de datos que necesitan XML en formato tabular
- **💼 Reportes Empresariales**: Conversión de datos de sistemas ERP/CRM
- **🔄 Migración de Datos**: Transferencia entre diferentes sistemas
- **📋 Auditorías**: Análisis de logs y registros en formato XML
- **🎓 Investigación Académica**: Procesamiento de datasets XML

---

## ⚡ Inicio Rápido

### 🚀 **En 3 Minutos**

```bash
# 1️⃣ Clonar repositorio
git clone https://github.com/jfGalvan/XMLtoExcelPro.git
cd XMLtoExcelPro

# 2️⃣ Instalar dependencias
pip install -r requirements.txt

# 3️⃣ ¡Convertir tu primer archivo!
python app.py ejemplo.xml resultado.xlsx
```

### 🖥️ **Interfaz Gráfica**
```bash
# Lanzar GUI
python ui.py
```

¡Arrastra tu archivo XML, elige destino y listo! 🎉

---

## 📦 Instalación Detallada

### 📋 **Requisitos Previos**

| Componente | Versión Mínima | Recomendada |
|------------|----------------|-------------|
| Python | 3.8+ | 3.9+ |
| RAM | 512MB | 2GB+ |
| Espacio en Disco | 100MB | 500MB+ |

### 🔧 **Instalación Completa**

<details>
<summary><strong>📦 Opción 1: Instalación Estándar</strong></summary>

```bash
# Clonar repositorio
git clone https://github.com/jfGalvan/XMLtoExcelPro.git
cd XMLtoExcelPro

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
python app.py --version
```
</details>

<details>
<summary><strong>🛡️ Opción 2: Con Entorno Virtual (Recomendada)</strong></summary>

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Clonar e instalar
git clone https://github.com/jfGalvan/XMLtoExcelPro.git
cd XMLtoExcelPro
pip install -r requirements.txt
```
</details>

<details>
<summary><strong>🐳 Opción 3: Con Docker</strong></summary>

```bash
# Construir imagen
docker build -t xmltoexcelpro .

# Ejecutar contenedor
docker run -v $(pwd):/data xmltoexcelpro input.xml output.xlsx
```
</details>

### 📋 **Dependencias Principales**

```txt
pandas>=1.5.0          # Manipulación de datos
openpyxl>=3.1.0        # Manejo de archivos Excel
lxml>=4.9.0            # Parser XML optimizado
tkinter                # Interfaz gráfica (incluido en Python)
xmltodict>=0.13.0      # Conversión XML a diccionario
progressbar2>=4.2.0    # Barras de progreso
colorama>=0.4.6        # Colores en terminal
```

---

## 🖥️ Modos de Uso

### 1️⃣ **Interfaz Gráfica (GUI)**

<div align="center">
<img src="https://via.placeholder.com/600x400/2196F3/white?text=GUI+Screenshot" alt="GUI Screenshot">
</div>

```bash
# Iniciar interfaz gráfica
python ui.py
```

**Características de la GUI:**
- 🎯 **Drag & Drop**: Arrastra archivos XML directamente
- 👀 **Vista Previa**: Previsualiza datos antes de convertir
- ⚙️ **Configuración Visual**: Ajusta opciones con interfaz intuitiva
- 📊 **Progreso Visual**: Barra de progreso en tiempo real
- 📁 **Explorador Integrado**: Navega y selecciona archivos fácilmente

### 2️⃣ **Línea de Comandos (CLI)**

#### **Sintaxis Básica**
```bash
python app.py <input.xml> <output.xlsx> [opciones]
```

#### **Opciones Disponibles**
```bash
# Opciones básicas
--sheet-name "NombreHoja"      # Nombre de la hoja Excel
--encoding utf-8               # Codificación del archivo XML
--delimiter ","                # Delimitador para datos CSV intermedios

# Opciones avanzadas
--preserve-hierarchy          # Mantiene estructura jerárquica XML
--include-attributes         # Incluye atributos XML como columnas
--max-rows 50000            # Máximo de filas por hoja
--split-sheets              # Divide en múltiples hojas si es necesario

# Opciones de formato
--date-format "YYYY-MM-DD"   # Formato de fechas
--number-format "0.00"       # Formato de números
--header-row                # Primera fila como encabezados

# Opciones de rendimiento
--batch-size 1000           # Tamaño de lote para procesamiento
--memory-limit 1024         # Límite de memoria en MB
--parallel                  # Procesamiento en paralelo

# Opciones de debugging
--verbose                   # Salida detallada
--debug                     # Modo debug completo
--log-file "conversion.log" # Archivo de log
```

### 3️⃣ **Programáticamente (API Python)**

```python
from xml_processor import XMLProcessor

# Crear instancia del procesador
processor = XMLProcessor()

# Configurar opciones
processor.configure(
    preserve_hierarchy=True,
    include_attributes=True,
    max_rows=50000
)

# Convertir archivo
result = processor.convert_xml_to_excel(
    input_file="data.xml",
    output_file="result.xlsx",
    sheet_name="Datos"
)

print(f"Conversión exitosa: {result.success}")
print(f"Filas procesadas: {result.rows_processed}")
```

---

## 💻 Ejemplos de Uso

### 📊 **Ejemplo 1: E-commerce - Catálogo de Productos**

**XML de Entrada:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<catalog>
  <product id="1" category="electronics">
    <name>Smartphone Galaxy</name>
    <price currency="USD">699.99</price>
    <stock>150</stock>
    <specifications>
      <screen>6.1 inches</screen>
      <storage>128GB</storage>
      <color>Black</color>
    </specifications>
  </product>
  <product id="2" category="electronics">
    <name>Laptop ThinkPad</name>
    <price currency="USD">1299.99</price>
    <stock>75</stock>
    <specifications>
      <screen>14 inches</screen>
      <storage>512GB SSD</storage>
      <color>Silver</color>
    </specifications>
  </product>
</catalog>
```

**Comando:**
```bash
python app.py catalog.xml products.xlsx \
  --sheet-name "Productos" \
  --include-attributes \
  --preserve-hierarchy
```

**Resultado Excel:**
| ID | Category | Name | Price | Currency | Stock | Screen | Storage | Color |
|----|----------|------|-------|----------|-------|---------|---------|-------|
| 1 | electronics | Smartphone Galaxy | 699.99 | USD | 150 | 6.1 inches | 128GB | Black |
| 2 | electronics | Laptop ThinkPad | 1299.99 | USD | 75 | 14 inches | 512GB SSD | Silver |

### 📈 **Ejemplo 2: Finanzas - Transacciones Bancarias**

```bash
# Procesar archivo grande con optimizaciones
python app.py transactions.xml bank_report.xlsx \
  --sheet-name "Transacciones_2024" \
  --batch-size 5000 \
  --memory-limit 2048 \
  --date-format "DD/MM/YYYY" \
  --verbose
```

### 🏢 **Ejemplo 3: Recursos Humanos - Empleados**

```bash
# Convertir con múltiples hojas
python app.py employees.xml hr_report.xlsx \
  --split-sheets \
  --max-rows 1000 \
  --sheet-name "Empleados"
```

### 🔄 **Ejemplo 4: Procesamiento por Lotes**

```bash
# Script para múltiples archivos
#!/bin/bash
for file in ./xml_files/*.xml; do
    filename=$(basename "$file" .xml)
    python app.py "$file" "./excel_output/${filename}.xlsx" \
      --verbose \
      --log-file "./logs/${filename}.log"
done
```

### 🐍 **Ejemplo 5: Integración Programática**

```python
import os
from xml_processor import XMLProcessor

def convert_xml_directory(input_dir, output_dir):
    """Convierte todos los XML de un directorio"""
    processor = XMLProcessor()
    
    for filename in os.listdir(input_dir):
        if filename.endswith('.xml'):
            xml_path = os.path.join(input_dir, filename)
            excel_path = os.path.join(output_dir, f"{filename[:-4]}.xlsx")
            
            try:
                result = processor.convert_xml_to_excel(xml_path, excel_path)
                print(f"✅ {filename}: {result.rows_processed} filas procesadas")
            except Exception as e:
                print(f"❌ {filename}: Error - {str(e)}")

# Uso
convert_xml_directory("./data/xml/", "./data/excel/")
```

---

## 📁 Estructura del Proyecto

```
XMLtoExcelPro/
│
├── 📄 README.md                 # Este archivo
├── 📋 requirements.txt          # Dependencias Python
├── 🐳 Dockerfile               # Contenedor Docker
├── ⚙️ setup.py                 # Configuración de instalación
├── 📜 LICENSE                  # Licencia MIT
└── 🚫 .gitignore              # Archivos ignorados por Git
│
├── 📂 src/                     # Código fuente principal
│   ├── 🚀 app.py               # Punto de entrada CLI
│   ├── 🖥️ ui.py                # Interfaz gráfica
│   ├── ⚙️ xml_processor.py     # Motor de procesamiento XML
│   ├── 📊 excel_writer.py      # Generador de archivos Excel
│   ├── 🖼️ embedded_images.py   # Manejo de imágenes embebidas
│   ├── ⚡ utils.py             # Utilidades y helpers
│   └── 📋 config.py           # Gestión de configuración
│
├── 📂 tests/                   # Pruebas unitarias
│   ├── test_xml_processor.py
│   ├── test_excel_writer.py
│   ├── test_ui.py
│   └── fixtures/              # Datos de prueba
│       ├── sample_simple.xml
│       ├── sample_complex.xml
│       └── expected_results/
│
├── 📂 examples/                # Ejemplos y casos de uso
│   ├── 🛒 ecommerce/
│   │   ├── products.xml
│   │   └── expected_output.xlsx
│   ├── 💰 finance/
│   │   ├── transactions.xml
│   │   └── expected_output.xlsx
│   └── 📋 tutorial/
│       ├── basic_example.xml
│       └── README.md
│
├── 📂 docs/                    # Documentación
│   ├── installation.md
│   ├── usage_guide.md
│   ├── api_reference.md
│   ├── troubleshooting.md
│   └── contributing.md
│
├── 📂 scripts/                 # Scripts de utilidad
│   ├── install.sh             # Script de instalación
│   ├── run_tests.sh          # Script de testing
│   └── build_docker.sh       # Script de construcción Docker
│
└── 📂 .github/                # Configuración GitHub
    ├── workflows/
    │   ├── ci.yml            # Integración continua
    │   └── release.yml       # Automatización de releases
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

---

## ⚙️ Configuración Avanzada

### 🔧 **Archivo de Configuración**

Crea un archivo `config.json` para personalizar el comportamiento:

```json
{
  "general": {
    "default_encoding": "utf-8",
    "temp_directory": "./temp",
    "log_level": "INFO"
  },
  "xml_processing": {
    "preserve_hierarchy": true,
    "include_attributes": false,
    "namespace_handling": "strip",
    "empty_elements": "skip"
  },
  "excel_output": {
    "default_sheet_name": "Sheet1",
    "max_rows_per_sheet": 50000,
    "auto_fit_columns": true,
    "include_index": false,
    "date_format": "YYYY-MM-DD",
    "number_format": "0.00"
  },
  "performance": {
    "batch_size": 1000,
    "memory_limit_mb": 1024,
    "enable_parallel": false,
    "max_workers": 4
  },
  "ui_settings": {
    "theme": "light",
    "window_size": "1024x768",
    "remember_last_directory": true
  }
}
```

### 🌍 **Variables de Entorno**

```bash
# Configuración global
export XMLTOEXCEL_CONFIG_FILE="/path/to/config.json"
export XMLTOEXCEL_LOG_LEVEL="DEBUG"
export XMLTOEXCEL_TEMP_DIR="/tmp/xmltoexcel"

# Configuración de rendimiento
export XMLTOEXCEL_MEMORY_LIMIT="2048"
export XMLTOEXCEL_MAX_WORKERS="8"
export XMLTOEXCEL_BATCH_SIZE="5000"

# Configuración de salida
export XMLTOEXCEL_DEFAULT_ENCODING="utf-8"
export XMLTOEXCEL_DATE_FORMAT="YYYY-MM-DD"
```

### 🎨 **Personalización de UI**

```python
# themes.json
{
  "dark_theme": {
    "background": "#2b2b2b",
    "foreground": "#ffffff",
    "accent": "#0078d4"
  },
  "light_theme": {
    "background": "#ffffff",
    "foreground": "#000000",
    "accent": "#0078d4"
  }
}
```

---

## 🧪 Testing

### 🚀 **Ejecutar Pruebas**

```bash
# Todas las pruebas
python -m pytest tests/

# Con cobertura
python -m pytest --cov=src tests/

# Pruebas específicas
python -m pytest tests/test_xml_processor.py -v

# Pruebas de integración
python -m pytest tests/integration/ -v
```

### 📊 **Tipos de Pruebas**

| Tipo | Descripción | Archivos |
|------|-------------|----------|
| **Unit** | Pruebas de funciones individuales | `test_*.py` |
| **Integration** | Pruebas de componentes integrados | `integration/` |
| **E2E** | Pruebas completas end-to-end | `e2e/` |
| **Performance** | Pruebas de rendimiento | `performance/` |

### 🎯 **Casos de Prueba Clave**

```python
# Ejemplo de prueba
def test_simple_xml_conversion():
    """Prueba conversión básica XML a Excel"""
    processor = XMLProcessor()
    result = processor.convert_xml_to_excel(
        "tests/fixtures/simple.xml",
        "tests/output/simple.xlsx"
    )
    assert result.success == True
    assert result.rows_processed > 0
```

---

## 🤝 Contribuir

¡Tu contribución hace la diferencia! 🌟

### 🚀 **Guía Rápida de Contribución**

1. **🍴 Fork** el repositorio
2. **🌿 Crear** una rama para tu feature: `git checkout -b feature/awesome-feature`
3. **💻 Desarrollar** tu mejora con tests
4. **✅ Verificar** que pasen todas las pruebas
5. **📝 Commit** con mensaje descriptivo: `git commit -m "feat: añadir soporte para XML namespaces"`
6. **🚀 Push** a tu rama: `git push origin feature/awesome-feature`
7. **🔄 Crear** un Pull Request

### 🎯 **Áreas de Contribución**

<table>
<tr>
<td width="25%">

#### 🐛 **Bug Fixes**
- Corrección de errores
- Mejoras de estabilidad
- Optimización de rendimiento

</td>
<td width="25%">

#### ✨ **Nuevas Features**
- Soporte para nuevos formatos
- Mejoras en UI/UX
- Funcionalidades avanzadas

</td>
<td width="25%">

#### 📖 **Documentación**
- Mejoras en README
- Tutoriales y guías
- Ejemplos de código

</td>
<td width="25%">

#### 🧪 **Testing**
- Casos de prueba adicionales
- Pruebas de integración
- Automatización de tests

</td>
</tr>
</table>

### 📋 **Checklist para Contribuidores**

- [ ] ✅ Código sigue PEP 8
- [ ] 🧪 Pruebas incluidas y pasan
- [ ] 📖 Documentación actualizada
- [ ] 🔄 Sin conflictos con main
- [ ] 📝 Commit messages descriptivos
- [ ] 🎯 Un feature por PR

### 🏆 **Hall of Fame**

Agradecimientos especiales a nuestros contribuidores:

<!-- CONTRIBUTORS-START -->
<a href="https://github.com/jfGalvan/XMLtoExcelPro/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=jfGalvan/XMLtoExcelPro" />
</a>
<!-- CONTRIBUTORS-END -->

---

## 🐛 Solución de Problemas

### ❓ **Problemas Comunes**

<details>
<summary><strong>🚨 Error: "ModuleNotFoundError: No module named 'pandas'"</strong></summary>

**Problema:** Dependencias no instaladas correctamente.

**Solución:**
```bash
pip install -r requirements.txt --force-reinstall
# o
pip install pandas openpyxl lxml
```
</details>

<details>
<summary><strong>💾 Error: "MemoryError" con archivos grandes</strong></summary>

**Problema:** Archivo XML demasiado grande para la memoria disponible.

**Soluciones:**
```bash
# Opción 1: Reducir batch size
python app.py large_file.xml output.xlsx --batch-size 500

# Opción 2: Aumentar límite de memoria
python app.py large_file.xml output.xlsx --memory-limit 4096

# Opción 3: Dividir en múltiples hojas
python app.py large_file.xml output.xlsx --split-sheets --max-rows 10000
```
</details>

<details>
<summary><strong>🔤 Error: "UnicodeDecodeError"</strong></summary>

**Problema:** Codificación incorrecta del archivo XML.

**Solución:**
```bash
# Especificar codificación correcta
python app.py file.xml output.xlsx --encoding iso-8859-1
# o
python app.py file.xml output.xlsx --encoding cp1252
```
</details>

<details>
<summary><strong>🖥️ Error: "GUI no se abre en Linux"</strong></summary>

**Problema:** Faltan dependencias gráficas.

**Solución:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# CentOS/RHEL
sudo yum install tkinter
```
</details>

### 🆘 **Obtener Ayuda**

| Canal | Descripción | Link |
|-------|-------------|------|
| 🐛 **GitHub Issues** | Reportar bugs y solicitar features | [Crear Issue](https://github.com/jfGalvan/XMLtoExcelPro/issues) |
| 💬 **Discussions** | Preguntas y discusiones | [GitHub Discussions](https://github.com/jfGalvan/XMLtoExcelPro/discussions) |
| 📧 **Email** | Soporte directo | xmltoexcelpro@gmail.com |
| 📖 **Wiki** | Documentación extensa | [GitHub Wiki](https://github.com/jfGalvan/XMLtoExcelPro/wiki) |

### 📊 **Diagnóstico Automático**

```bash
# Script de diagnóstico
python -c "
import sys
import pkg_resources
import platform

print('=== XMLtoExcelPro Diagnóstico ===')
print(f'Python: {sys.version}')
print(f'SO: {platform.system()} {platform.release()}')
print('Paquetes instalados:')
for pkg in ['pandas', 'openpyxl', 'lxml']:
    try:
        version = pkg_resources.get_distribution(pkg).version
        print(f'  {pkg}: {version} ✅')
    except:
        print(f'  {pkg}: No instalado ❌')
"
```

---

## 🗺️ Roadmap

### 🎯 **Próximas Versiones**

#### **v2.0 - Q2 2024**
- [ ] 🌐 Soporte para JSON como formato de salida
- [ ] 🔄 Conversión bidireccional (Excel → XML)
- [ ] 🎨 Nueva interfaz gráfica con tema moderno
- [ ] ⚡ Procesamiento en paralelo nativo

#### **v2.1 - Q3 2024**
- [ ] 🌍 Interfaz web con Flask/FastAPI
- [ ] 🔗 API REST para integraciones
- [ ] 📊 Dashboard de estadísticas
- [ ] 🤖 Detección automática de esquemas XML

#### **v2.2 - Q4 2024**
- [ ] 🗄️ Soporte para bases de datos (SQL Server, MySQL, PostgreSQL)
- [ ] 📈 Visualizaciones integradas con Plotly
- [ ] 🔒 Encriptación de archivos sensibles
- [ ] 🐳 Imagen Docker oficial

### 🌟 **Visión a Largo Plazo**
- **Integración con Cloud**: AWS S3, Google Drive, Azure Blob
- **Machine Learning**: Detección automática de patrones en XML
- **Plugins**: Sistema de extensiones para formatos personalizados
- **Multiplataforma**: Aplicaciones nativas para Windows/macOS/Linux

---

## 📊 Estadísticas del Proyecto

<div align="center">

![GitHub Stats](https://github-readme-stats.vercel.app/api?username=jfGalvan&repo=XMLtoExcelPro&show_icons=true&theme=default)

![Languages](https://github-readme-stats.vercel.app/api/top-langs/?username=jfGalvan&layout=compact)

</div>

---

## 📄 Licencia

Este proyecto está licenciado bajo la **Licencia MIT** - ver el archivo [LICENSE](LICENSE) para más detalles.

```
MIT License

Copyright (c) 2024 jfGalvan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 👨‍💻 Autor y Reconocimientos
