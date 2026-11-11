# Trabajo Practico Integrador 2 Satelites
Alumno: Ricardo Maldonado

# Descripcion:
Se desarrolla un programa de línea de comandos que lee un archivo con los satélites activos, obtiene la posición de cada uno, lo representa con un objeto y permite hacer un resumen de todos o consultar por zona

# Comandos en terminal
Los comandos para ejecutar las consultas son los siguientes:
- Para generar el resumen con todos los satelites: python consultar_satelites.py datos/satelites.json resumen
- Para generar un python consultar_satelites.py datos/satelites.json zona
- Para ejecutar test_* (muestra una tabla y ademas genera la url): pytest --cov=satelite --cov=catalogo --cov-report=term-missing --cov-report=html

# Completar el README: nombre, descripción y cómo ejecutar las consultas y las pruebas.