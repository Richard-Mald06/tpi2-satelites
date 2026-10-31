class Satelite:
    def __init__(self, nombre, num_catalogo, latitud, longitud, altitud):

        if not -90<=latitud<=90:
            raise ValueError("latitud no valida (fuera de rango)")

        if not -180<=longitud<=180:
            raise ValueError("longitud no valida (fuera de rango)")

        if not 100<=altitud:
            raise ValueError("altitud fuera de rango")

        if not isinstance(nombre, str) or len(nombre.strip()) == 0:
            raise ValueError("nombre no válido")

        if not isinstance(num_catalogo, int) or isinstance(num_catalogo, bool):
            raise ValueError("número de catálogo no válido")
        
        self.nombre = nombre 
        self.num_catalogo = num_catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud


    def tipo_orbita(self):
        if self.altitud < 2000:
            return "LEO"
        elif 2000 <= self.altitud < 34000:
            return "MEO"
        elif 34000 <= self.altitud <= 37000:
            return "GEO"
        else:
            return "HEO"

    def descripcion(self):
        return f"{self.nombre} | {self.num_catalogo} | {self.tipo_orbita()} | {self.altitud} km"

    def zona_valida(self, longitud_min, latitud_min, longitud_max, latitud_max):
        if longitud_min <= self.longitud <= longitud_max and latitud_min <= self.latitud <= latitud_max:
            return True
        return False