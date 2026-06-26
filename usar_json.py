import json

ARCHIVO = "alumnos.json"

def leer_json():

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            alumnos = json.load(archivo)

            return alumnos

def modificar_json(alumnos):

    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(alumnos, archivo, indent=4, ensure_ascii=False)

        return alumnos
