from cargar_alumnos import meter_alumno
from usar_json import leer_json
from buscar_alumno import buscar
from modificar_alumno import mod_alumno
from eliminar_alumno import del_alumno
from estadisticas import stats_alumno

def menu():

    ban = 1

    while ban == 1:

        opcion = int(input(        
        "1) cargar alumno\n"
        "2) ver lista de alumnos\n"
        "3) buscar alumno\n"
        "4) modificar perfil de alumno\n"
        "5) eliminar alumno\n"
        "6) ver estadisticas\n"
        "7) salir\n"
        "que quiere hacer?: "
))

        match opcion:
            case 1:
                while ban == 1:
                    dni = int(input("\ndame el dni del alumno: ")) 

                    if 9999999 < dni < 900000000: #por aca si el dni no coincide con los 8 digitos debe intentarlo de nuevo
                        dni = str(dni) #lo paso como str para que si ya existe el dni lo reconozca y te diga que ya existe
                        meter_alumno(dni)
                        break

                    else:
                        print("opcion fuera de rango, intente de nuevo. ")

            case 2:
                alumnos = leer_json()

                for dni in alumnos: #aca simplemente lee el json con toda la info
                    datos = alumnos[dni]
                    print("-" * 20)
                    print(f"DNI: {dni}")
                    print(f"Nombre: {datos["nombre"]}")
                    print(f"Apellido: {datos["apellido"]}")
                    print(f"Edad: {datos["edad"]}")
                    print(f"Nota: {datos["nota"]}")
                    print("-" * 20)

            case 3:
                dni = input("vamos a buscarlo por dni: ")
                buscar(dni)
            case 4:
                dni = input("vamos a modificar por dni: ")
                mod_alumno(dni)
            case 5:
                dni = input("vamos a eliminar por dni: ")
                del_alumno(dni)
            case 6:
                stats_alumno()
            case 7:
                print("\nadios")
                return