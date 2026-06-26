from usar_json import leer_json

def buscar(dni):

    alumnos = leer_json()

    if dni in alumnos:
        print("<" * 20)
        print(f"DNI: {dni}")
        print(f"Nombre: {alumno['nombre']}")
        print(f"Apellido: {alumno['apellido']}")
        print(f"Edad: {alumno['edad']}")
        print(f"Nota: {alumno['nota']}")
        print("<" * 20)

    else:
        print("No se encontró el alumno")