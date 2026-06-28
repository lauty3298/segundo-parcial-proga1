import json

ARCHIVO = "alumnos.json" #ruta fija del json

def leer_json(): #aca todos pasan a leer el json

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            alumnos = json.load(archivo)

            return alumnos

def modificar_json(alumnos): #y aca todos pasan con sus modificaciones

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)

        return alumnos
