from catalogo import leer_json, crear_catalogo, resumir_por_orbita, satelites_en_zona
from satelite import Satelite
import pytest

def test_leer_json():
    registros = leer_json("datos/satelites.json")
    assert len(registros) == 16710

registro_valido = {
    "OBJECT_NAME": "CALSPHERE 1",
    "OBJECT_ID": "1964-063C",
    "EPOCH": "2026-10-14T14:21:25.466688",
    "MEAN_MOTION": 13.76730837,
    "ECCENTRICITY": 0.00243553,
    "INCLINATION": 90.2208,
    "RA_OF_ASC_NODE": 74.5342,
    "ARG_OF_PERICENTER": 291.4443,
    "MEAN_ANOMALY": 198.023,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "NORAD_CAT_ID": 900,
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 8785,
    "BSTAR": 0.00056429819,
    "MEAN_MOTION_DOT": 5.64e-06,
    "MEAN_MOTION_DDOT": 0
}
def test_crear_catalogo():
    lista = crear_catalogo([registro_valido])

    assert len(lista) == 1
    assert lista[0].nombre == "CALSPHERE 1"
    assert lista[0].num_catalogo == 900

#registro sin numero de catalogo
registro_invalido = {
    "OBJECT_NAME": "CALSPHERE 1",
    "OBJECT_ID": "1964-063C",
    "EPOCH": "2026-10-14T14:21:25.466688",
    "MEAN_MOTION": 13.76730837,
    "ECCENTRICITY": 0.00243553,
    "INCLINATION": 90.2208,
    "RA_OF_ASC_NODE": 74.5342,
    "ARG_OF_PERICENTER": 291.4443,
    "MEAN_ANOMALY": 198.023,
    "EPHEMERIS_TYPE": 0,
    "CLASSIFICATION_TYPE": "U",
    "ELEMENT_SET_NO": 999,
    "REV_AT_EPOCH": 8785,
    "BSTAR": 0.00056429819,
    "MEAN_MOTION_DOT": 5.64e-06,
    "MEAN_MOTION_DDOT": 0
}

def test_crear_catalogo_registro_invalido():
    lista = crear_catalogo([registro_invalido])
    assert len(lista) == 0


def test_resumir_por_orbita():
    assert resumir_por_orbita([]) == {}

def test_resumir_por_orbita_con_satelites():
    lista = [Satelite("satelite1", 1, 0, 0, 500), Satelite("satelite2", 2, 0, 0, 700)]
    resumen = resumir_por_orbita(lista)

    assert resumen["LEO"]["cantidad"] == 2
    assert resumen["LEO"]["minimo"] == 500
    assert resumen["LEO"]["maximo"] == 700
    assert resumen["LEO"]["promedio"] == 600

def test_satelites_en_zona():
    valido = Satelite("adentro", 1, 5, 5, 500)
    no_valido = Satelite("afuera", 2, 50, 50, 500)

    resultado = satelites_en_zona([valido, no_valido], 0, 0, 10, 10)

    assert len(resultado) == 1
    assert resultado[0].nombre == "adentro"