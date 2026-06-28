from usar_json import leer_json

def buscar(dni):

    alumnos = leer_json()

    if dni in alumnos: # para mas simplicidad siempre que se busque a alguien pedimos el dni y aca se encuentra, mostrando todos los datos, este ejemplo lo vi del profe y ya dijo que hagamos lo que queramos asique sin quejas no?
        print("<" * 20)
        print(f"DNI: {dni}")
        print(f"Nombre: {alumno["nombre"]}")
        print(f"Apellido: {alumno["apellido"]}")
        print(f"Edad: {alumno["edad"]}")
        print(f"Nota: {alumno["nota"]}")
        print("<" * 20)

    else:
        print("No se encontró el alumno")