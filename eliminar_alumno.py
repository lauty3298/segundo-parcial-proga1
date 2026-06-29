from usar_json import leer_json, modificar_json

def del_alumno(dni):

    alumnos = leer_json()

    if dni in alumnos: 
       
        alumnos.pop(dni) #aca el alumno hace pop y desaparece

        modificar_json(alumnos)

        print("Alumno eliminado correctamente.\n")

        return 

    else:
        print("No se encontró el alumno")