# Trabajo Practico Integrador 2 Satelites
Alumno: Ricardo Maldonado

# Descripcion:
Se desarrolla un programa de línea de comandos que lee un archivo con los satélites activos, obtiene la posición de cada uno, lo representa con un objeto y permite hacer un resumen de todos o consultar por zona.

# Elementos
En satelite.py se crea la clase Satelite con los metodos:
- tipo_orbita(): Segun la altitud define el tipo de orbita de cada satelite
- descripcion(): crea un str que contiene el nombre, numero de catalogo, el tipo de orbita y la altitud de cada satelite
- zona_valida(): en caso de consultar una zona, verifica si estan dentro de la zona o no

En catalogo.py se crean las funciones:
- leer_json(): Recibe la ruta del json y carga los registros en una variable
- crear_catalogo(): Recibe los registros y los valida, en caso de ser validos se agregan a una lista
- resumir_por_orbita(): Recibe la lista de validos y los separa por tipo de orbita, ademas crea un resumen con datos de cata tipo
- satelites_en_zona(): Recibe la lista de satelites si estan dentro del area de esa zona y los agrega a una lista

En funciones_base.py:
Codigo proporcionado por el profesor, devuelve una tupla con los valores de latitud, longitud, altitud convertidos a float

consultar_satelites.py es el codigo principal, llama a las clases, metodos y funciones de los archivos mencionados anteriormente

# Comandos en terminal
Los comandos para ejecutar las consultas son los siguientes:
- Para generar el resumen con todos los satelites: python consultar_satelites.py datos/satelites.json resumen
- Para generar un python consultar_satelites.py datos/satelites.json zona
- Para ejecutar test_* (muestra una tabla y ademas genera la url): pytest --cov=satelite --cov=catalogo --cov-report=term-missing --cov-report=html