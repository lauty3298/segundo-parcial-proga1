from usar_json import leer_json, modificar_json

def meter_alumno(dni):

    alumnos = leer_json()

    if dni in alumnos:
        print("el alumno ya existe. \n")
    
    else:
        alumnos[dni] = {
            "nombre": input("Nombre: "),
            "apellido": input("Apellido: "),
            "edad": int(input("Edad: ")),
            "nota": float(input("Nota: "))
        }

        modificar_json(alumnos)

        print("Alumno agregado correctamente.\n")
        print("-" * 15)
    
    

    

    