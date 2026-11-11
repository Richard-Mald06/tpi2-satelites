from satelite import Satelite
import pytest

def test_descripcion_satelite_valido():
    sat = Satelite("CALSPHERE 1", 900, -71.002, -132.691, 984.495)

    resultado = sat.descripcion()

    assert resultado == "CALSPHERE 1 | 900 | LEO | 984.495 km"


def test_tipo_orbita_leo():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 900)
    assert sat.tipo_orbita() == "LEO"

def test_tipo_orbita_leo_borde():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 1999.9)
    assert sat.tipo_orbita() == "LEO"

def test_tipo_orbita_meo():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 5000)
    assert sat.tipo_orbita() == "MEO"

def test_tipo_orbita_meo_borde_inferior():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 2000)
    assert sat.tipo_orbita() == "MEO"

def test_tipo_orbita_meo_borde_superior():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 33999.9)
    assert sat.tipo_orbita() == "MEO"

def test_tipo_orbita_geo():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 36000)
    assert sat.tipo_orbita() == "GEO"

def test_tipo_orbita_geo_borde_inferior():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 34000)
    assert sat.tipo_orbita() == "GEO"

def test_tipo_orbita_geo_borde_superior():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 37000)
    assert sat.tipo_orbita() == "GEO"

def test_tipo_orbita_heo():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 40000)
    assert sat.tipo_orbita() == "HEO"

def test_tipo_orbita_heo_borde():
    sat = Satelite("CALSPHERE 1", 0, 0, 0, 37000.1)
    assert sat.tipo_orbita() == "HEO"


def test_latitud_invalida():
    with pytest.raises(ValueError):
        Satelite("CALSPHERE 1", 0, 91, 100, 30000)

def test_longitud_invalida():
    with pytest.raises(ValueError):
        Satelite("CALSPHERE 1", 0, 50, 181, 30000)

def test_altitud_invalida():
    with pytest.raises(ValueError):
        Satelite("CALSPHERE 1", 0, 50, 100, 99)

def test_nombre_vacio():
    with pytest.raises(ValueError):
        Satelite("", 0, 50, 100, 500)

def test_num_catalogo_invalido():
    with pytest.raises(ValueError):
        Satelite("CALSPHERE 1", "abc", 50, 100, 500)

def test_zona_valida():
    sat = Satelite("CALSPHERE 1", 0, 5, 5, 200)
    assert sat.zona_valida(0, 0, 10, 10)

def test_zona_valida_borde_latitud():
    sat = Satelite("CALSPHERE 1", 0, 10, 5, 200)
    assert sat.zona_valida(0, 0, 10, 10)

def test_zona_valida_borde_longitud():
    sat = Satelite("CALSPHERE 1", 0, 5, 10, 200)
    assert sat.zona_valida(0, 0, 10, 10)

def test_zona_invalida():
    sat = Satelite("CALSPHERE 1", 0, 11, 11, 200)
    assert not sat.zona_valida(0, 0, 10, 10)