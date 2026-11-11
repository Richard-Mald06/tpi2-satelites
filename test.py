from catalogo import leer_json, crear_catalogo, resumir_por_orbita, satelites_en_zona  # ajustá los nombres a los tuyos
from funciones_base import obtener_posicion
from satelite import Satelite

registros = leer_json("datos/satelites.json")
lista = crear_catalogo(registros)
# print(len(registros), len(lista))

resumen = resumir_por_orbita(lista)

print(resumen)

en_zona = satelites_en_zona(lista, -76.30, -46.13, -66.30, -36.13)
print(len(en_zona))


registros = leer_json("datos/satelites.json")
print(obtener_posicion(registros[0]))

sat = Satelite("CALSPHERE 1" , 900, -71.002, -132.691, 984.495)

print(sat.descripcion())