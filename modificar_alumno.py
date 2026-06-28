from usar_json import leer_json, modificar_json

def mod_alumno(dni):
    
    alumnos = leer_json()

    if dni in alumnos: #aca estan conbinadas las funciones de busquedad y agragar
        alumnos[dni] = {
        "nombre": input("Nombre: "),
        "apellido": input("Apellido: "),
        "edad": int(input("Edad: ")),
        "nota": float(input("Nota: "))
    }

        modificar_json(alumnos)

        print("Alumno agregado correctamente.\n")

        return

    else:
        print("No se encontró el alumno")