import sys

from catalogo import leer_json, crear_catalogo, resumir_por_orbita, satelites_en_zona

# ejecutar en terminal
# python consultar_satelites.py datos/satelites.json resumen
# python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13

def main():
    if len(sys.argv) < 3:
        print("comando de consola con argumentos insuficientes")
        sys.exit(1)

    consulta = sys.argv[2]
    if consulta == "resumen":
        if len(sys.argv) != 3:
            print("comando no valido, no se puede hacer el resumen")
            sys.exit(1)

    elif consulta == "zona":
        if len(sys.argv) != 7:
            print("comando no valido, no se puede verificar la zona")
            sys.exit(1)
        try:
            longitud_min = float(sys.argv[3])
            latitud_min = float(sys.argv[4])
            longitud_max = float(sys.argv[5])
            latitud_max = float(sys.argv[6])
        except ValueError:
            print("Los datos ingresados en zona no son numericos")
            sys.exit(1)

    else:
        print("comando no valido, las consultas validas son resumen y zona")
        sys.exit(1)

    ruta_json = sys.argv[1]

    #lectura de la ruta del json y se guardan los datos crudos
    try:
        registros = leer_json(ruta_json)
    except FileNotFoundError:
        print("El archivo que se intenta leer no existe")
        sys.exit(1)

    lista = crear_catalogo(registros)
    if consulta == "resumen":
        resumen = resumir_por_orbita(lista)
        #recorre diccionario de diccionarios ej: {"LEO":{'cantidad':0, 'minimo':0, 'maximo':0, 'promedio':0}}
        for tipo, datos in resumen.items():
            print(f"datos del tipo {tipo}:")
            #recorre el diccionario que estaba dentro, ahora las keys son cantidad, maximo, minimo, promedio
            for clave, valor in datos.items():
                print(f"- {clave.capitalize()}: {valor}")

    elif consulta == "zona":
        lista_zona = satelites_en_zona(lista, longitud_min, latitud_min, longitud_max, latitud_max)
        print(f"satelites en la zona {len(lista_zona)}")
        for sat in lista_zona:
            print(sat.descripcion())


main()