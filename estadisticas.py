from usar_json import leer_json

def stats_alumno():

    alumnos = leer_json()

    promedio = 0
    mejor_nota = 0
    aprobados = 0

    for dni in alumnos: #aca recorremos el diccionario:
        datos = alumnos[dni] #la suma de todas las notas para sacar un promedio

        promedio += datos["nota"]
        
        if mejor_nota < datos["nota"]: 
            mejor_nota = datos["nota"] #quien tiene la mejor
            mejor_alumno = datos["nombre"] #y quien es, si para el ejemplo salgo yo fue sin querer queriendo
        
        if datos["nota"] <= 6: #si la nota supera o es igual a 6 aprueban
            aprobados += 1
     
    print(f"\ntenemos {len(alumnos)} alumnos.")
    print(f"el promedio es de {promedio / len(alumnos)}")
    print(f"el que tiene la mejor nota es {mejor_alumno} con un {mejor_nota} ")
    print(f"tenemos {aprobados} alumnos que aprobaron ")
    print("_" * 20 )