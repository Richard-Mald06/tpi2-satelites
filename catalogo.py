import json
import  funciones_base as func
from satelite import Satelite

def leer_json(ruta_json):
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
        return datos

def crear_catalogo(datos):
    lista = []
    for dato in datos:
        latitud, longitud, altitud = func.obtener_posicion(dato)
        try:
            sat = Satelite(dato["OBJECT_NAME"], dato["NORAD_CAT_ID"], latitud, longitud, altitud)
            lista.append(sat)

        except ValueError:
            pass
    return lista