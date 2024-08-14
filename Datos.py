import json

ruta="usuarios.json"

def guardar_datos(datos):
    try:
        with open(ruta, "w") as file:
            json.dump(datos, file, indent=4)
    except Exception as err:
        print("ERROR AL GUARDAR DATOS", err)
        print("****************************************************************************************")

def cargar_datos():
    try:
        with open(ruta, "r") as archivito:
            datos = json.load(archivito)
            return datos
    except Exception as err:
        print("ERROR AL CARGAR DATOS", err)
        print("****************************************************************************************")
