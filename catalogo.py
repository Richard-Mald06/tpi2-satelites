import json
import funciones_base as func
from satelite import Satelite

def leer_json(ruta_json):
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos

def crear_catalogo(registros):
    lista = []
    contador_errores = 0
    for registro in registros:
        try:
            latitud, longitud, altitud = func.obtener_posicion(registro)
            nombre = registro["OBJECT_NAME"]
            num_catalogo = registro["NORAD_CAT_ID"]
            sat = Satelite(nombre, 
                           num_catalogo, 
                           latitud, 
                           longitud, 
                           altitud)
            lista.append(sat)
        except (ValueError, KeyError):
            contador_errores +=1
            continue
    #devuelve una lista de satelites
    print(f"se excluyeron {contador_errores} satelites por falta de datos/errores")
    return lista

def resumir_por_orbita(lista):
    tipos = {"LEO": [],
             "MEO": [],
             "GEO": [],
             "HEO": []}
    for sat in lista:
        tipos[sat.tipo_orbita()].append(sat.altitud)

    resumen = {}
    for tipo, altitudes in tipos.items():
        cantidad = len(altitudes)

        #verificacion de que altitudes no es una lista vacia
        if cantidad == 0:
            continue
        minimo = altitudes[0]
        maximo = altitudes[0]

        for altitud in altitudes:
            if minimo > altitud:
                minimo = altitud
            if maximo < altitud:
                maximo = altitud
        promedio = sum(altitudes)/cantidad
        #armado del diccionario de diccionarios el tipo es la clave, el diccionario de datos el valor
        resumen[tipo] = {
            "cantidad": cantidad,
            "minimo": minimo,
            "maximo": maximo,
            "promedio": promedio
        }
    return resumen

def satelites_en_zona(lista, longitud_min, latitud_min, longitud_max, latitud_max):
    lista_zona = []
    for satelite in lista:
        if satelite.zona_valida(longitud_min, latitud_min, longitud_max, latitud_max):
            lista_zona.append(satelite)
    return lista_zona