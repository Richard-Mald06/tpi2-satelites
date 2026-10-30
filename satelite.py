class Satelite:
    def __init__(self, nombre, num_catalogo, latitud, longitud, altitud):
        self.nombre = nombre 
        self.num_catalogo = num_catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def verificar_latitud(self):
        return -90<self.latitud<90 
    def verificar_longitud(self):
        return -180<=self.longitud<=180
    def verificar_altitud(self):
        return 100<=self.altitud