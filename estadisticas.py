from usar_json import leer_json

def stats_alumno():

    alumnos = leer_json()

    promedio = 0
    mejor_nota = 0
    mejor_alumno = ""
    aprobados = 0

    for dni, datos in alumnos.items():
        promedio += datos["nota"]

        if mejor_nota < datos["nota"]:
            mejor_nota = datos["nota"]
            mejor_alumno = datos["nombre"]
        
        if datos["nota"] <= 6:
            aprobados += 1
     
    print(f"\ntenemos {len(alumnos)} alumnos.")
    print(f"el promedio es de {promedio / len(alumnos)}")
    print(f"el que tiene la mejor nota es {mejor_alumno} con un {mejor_nota} ")
    print(f"tenemos {aprobados} alumnos que aprobaron ")
    print("_" * 20 )