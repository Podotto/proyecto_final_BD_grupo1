🚀 Log Analyzer
Convierte datos complejos en decisiones inteligentes
Log Analyzer es una herramienta diseñada para analizar registros de actividad (logs) de manera rápida y sencilla. Permite transformar grandes cantidades de datos en información clara, útil y fácil de interpretar.
Este sistema ayuda a identificar comportamientos importantes dentro de un sistema, como accesos exitosos, intentos fallidos y posibles actividades sospechosas, facilitando la toma de decisiones.
✨ Características
•	Lectura de logs
•	Análisis automático de registros
•	Resumen claro de la actividad del sistema
•	Identificación de accesos exitosos
•	Detección de intentos fallidos
•	Identificación de posibles comportamientos sospechosos
•	Ranking de usuarios con mayor actividad
•	Generación de reportes listos para revisar
•	Uso sencillo mediante menú interactivo
📁 Arquitecura del proyecto
El programa está organizado de forma clara para facilitar su uso y mantenimiento:
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
🛠️ Tecnologías utilizadas
•	Python
•	Manejo de archivos de texto
•	Procesamiento de datos
Instalación
El programa es ligero y no requiere instalaciones complejas.
Solo necesitas:
1.	Clonar el repositorio
Git clone https://github.com/Podotto/proyecto_final_BD_grupo1.git
2.	Ubicarse en la carpeta del proyecto
3.	Ejecutar el programa con Python utilizando el comando python -m src.menu
En pocos segundos estará listo para usarse.
🔄 Flujo de la aplicación
El programa funciona mediante un menú interactivo que guía al usuario paso a paso:
1.	Cargar los registros desde el archivo
2.	Procesar la información
3.	Analizar los datos obtenidos
4.	Generar un reporte con los resultados
El usuario solo necesita seleccionar las opciones del menú para obtener el análisis completo.
💡 Casos de uso
•	Monitoreo de actividad en sistemas informáticos
•	Identificación de intentos de acceso no autorizados
•	Análisis de comportamiento de usuarios
•	Apoyo en auditorías básicas de seguridad
•	Revisión rápida de grandes volúmenes de registros
🚀 Futuras mejoras
•	Interfaz gráfica más visual e intuitiva
•	Gráficos y estadísticas en tiempo real
•	Soporte para múltiples formatos de archivos
•	Exportación de reportes en PDF y Excel
•	Integración con sistemas en vivo
Seguridad
Log Analyzer está diseñado para trabajar de forma segura y confiable:
•	Los datos se procesan localmente, sin enviarse a internet
•	No se requiere acceso a información sensible del sistema
•	Los archivos originales no son modificados
•	Los resultados se generan en un archivo separado para mayor control
Esto garantiza que la información analizada se mantenga privada y bajo control del usuario.
👥 Autores
Desarrollado por Alexis Castillo, Técnico Superior en Big Data y Ciencia de Datos, y Grethel Halphen, Técnica Superior en Big Data y Ciencia de Datos


****
