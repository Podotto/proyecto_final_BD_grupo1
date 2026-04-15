# 🚀Log Analyzer
## _Convierte datos complejos en decisiones inteligentes_

Log Analyzer es una herramienta diseñada para analizar registros de acividad (logs) de manera rápida y sencilla. Peermite transformar grandes cantidades de datos en información clara, útil y fácil de interpretar.

Este sistema ayuda a identificar comportamientos importantes dentro de un sistema, como accesos exitosos, intentos fallidos, eventos ejecutados y posibles actividades sospechosas, facilitando la toma de decisiones.

## ✨Características

- 📖 Lectura de logs
- 📈 Análisis automático de registros
- 💻 Resumen claro de la actividad del sistema
- ✅ Identificación de accesos exitosos
- ❌ Detección de intentos fallidos
- ⚠️ Identificación de posibles comportamientos sospechosos
- 📊 Estadísticas de usuarios con mayor actividad
- 📄 Generación de reportes listos para revisar
- 🎯 Uso sencillo mediante un menú interactivo

## 🗂️Arquitectura del Proyecto

El programa está organizado de forma clara para facilitar su uso y mantenimiento.

```
log-analyzer/
│
├── data/
│ └── logs.txt
│
├── src/
│ ├── main.py
│ ├── reader.py
│ ├── processor.py
│ ├── analyzer.py
│ ├── reporter.py
│
└── output/
 └── reporte.txt
```

## 🛠️Tecnologías Utilizadas

- Python (lógica de programación)
- Manejo de archivos de texto (.txt)
- Procesamiento de datos
- Estructuras de datos básicas (listas y diccionarios)

## ⬇️Instalación

El programa es ligero y no requiere instalaciones complejas. Solo se necesita:

1. Clonar el respositorio
```
git clone https://github.com/Podotto/proyecto_final_BD_grupo1.git
```
2. Ubicarse en la carpeta del proyecto
3. Ejecutar el programa con Python utilizando el comando
```
python -m src.menu
```

En pocos segundos estará listo para utilizarse.

## 🔀Flujo de la Aplicación

El programa funciona mediante un menú interactivo que guía al usuario paso a paso:

1. Cargar los registros desde el archivo ubicado en la carpeta 'data'
2. Procesar la información
3. Analizar los datos obtenidos
4. Generar un reporte con los resultados en la carpeta 'output'

El usuario solo necesita seleccionar las opciones del menú para obtener el análisis completo.

## 💡Casos de Uso

- 🔎 Monitoreo de actividad en sistemas informáticos
- 🔒 Identificación de intentos de acceso no autorizados
- 👤 Análisis de comportamiento de usuarios
- 🕵 Apoyo en auditorías básicas de seguridad
- 🗃️ Revisión rápida de grandes volúmenes de registros

## 🔜Futuras Mejoras

- Interfaz gráfica más visual e intuitiva
- Gráficos y estadísticas en tiempo real
- Análisis de múltiples archivos en tiempo real
- Soporte para múltiples formatos de archivos
- Exportación de reportes en PDF y Excel
- Integración con sistemas en vivo

## 🛡️Seguridad

Log Analyzer está diseñado para trabajar de forma segura y confiable:

- Los datos se procesan fácilmente, sin enviarse a Internet
- No se requiere acceso a información sensible del sistema
- Los archivos originales no son modificados
- Los resultados se generan en un archivo separado para mayor control

Esto garantiza que la información analizada se mantenga privada y bajo control del usuario

## 👥Autores

Desarrollado por Alexis Castillo y Grethel Halphen, Especialistas en Big Data y Ciencia de Datos.
