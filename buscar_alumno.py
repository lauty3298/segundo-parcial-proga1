from usar_json import leer_json

def buscar(dni):

    alumnos = leer_json()

    if dni in alumnos:          # para mas simplicidad siempre que se busque a alguien pedimos el dni y aca se encuentra
        datos = alumnos[dni]

        print("-" * 20)
        print(f"DNI: {dni}")
        print(f"Nombre: {datos["nombre"]}")
        print(f"Apellido: {datos["apellido"]}")
        print(f"Edad: {datos["edad"]}")
        print(f"Nota: {datos["nota"]}")
        print("-" * 20)

    else:
        print(">>> No se encontró el alumno")

        