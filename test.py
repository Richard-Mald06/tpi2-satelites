from catalogo import leer_json, crear_catalogo, resumir_por_orbita, satelites_en_zona  # ajustá los nombres a los tuyos

registros = leer_json("datos/satelites.json")
lista = crear_catalogo(registros)
# print(len(registros), len(lista))

resumen = resumir_por_orbita(lista)

print(resumen)

en_zona = satelites_en_zona(lista, -76.30, -46.13, -66.30, -36.13)
print(len(en_zona))