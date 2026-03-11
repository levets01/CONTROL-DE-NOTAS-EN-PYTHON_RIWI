print("░█▀▀░▀█▀░█▀▀░▀█▀░█▀▀░█▄█░█▀█░░░█▀▄░█▀▀░░░█▀▀░█▀█░█▀█░▀█▀░█▀▄░█▀█░█░░░░░█▀▄░█▀▀░░░█▀█░█▀█░▀█▀░█▀█░█▀▀ ")
print("░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█░█▀█░░░█░█░█▀▀░░░█░░░█░█░█░█░░█░░█▀▄░█░█░█░░░░░█░█░█▀▀░░░█░█░█░█░░█░░█▀█░▀▀█ ")
print("░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀░▀░░░▀▀░░▀▀▀░░░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀ ")

#aca esta la lista en la que se almacenan los estudiantes
estudiantes = []
#aca estan las variasbles donde se van a almacenar los datos de los couder 
suma_notas = 0
reprobados = 0
regulares = 0
execelentes = 0
mejor_nota = 0
mejor_couder = ""

modulos = input("\n INGRESE EL NOMBRE DEL MODULO: ")
cantidad = int(input("INGRESE LA CANTIDAD DE COUDER: "))


# Aqui cree una funcion para la validacion el numero debe estar entre 0 a 100

def validar_nota(mensaje):
    while True:
        nota = float(input(mensaje))
if 0 <= nota <= 100 :
            return nota
        else:
            print("ERROR LA NOTA DEBE ESTAR ENTRE 0 Y 100 ")

for i in range (cantidad):
    print("\n COUDER", i+1)

    nombre = input ("INGRESE EL NOMBRE DEL COUDER : ")


    desarrollo = validar_nota ("INGRESE LA NOTA DE DESARROLLO")
    ingles = validar_nota ("INGRESE LA NOTA DE INGLES: ")
    habilidades = validar_nota ("INGRESE LA NOTA DE HABILIDADES: ")

    if input == "*" :
        break




    nota_final = (desarrollo * 0.6 ) + (ingles * 0.2) + (habilidades *0.2)
    
    suma_notas += nota_final
    
    if nota_final <50:
        clasificacion = "Reprobado"
        reprobados += 1
        
    elif nota_final < 80 :
        clasificacion = "Regular"
        regulares += 1
        
    else:
        clasificacion = "Excelente"
        excelentes  += 1
        
        if nota_final > mejor_nota:
            mejor_nota = nota_final
            mejor_coder = nombre
            
            
            
        
        
    estudiante = {
                "nombre" : nombre,
                "nota_final" : nota_final,
                "clasificacion" : clasificacion
            }
    estudiantes.append(estudiante)
    
    
print ("\n RESULTADOS")

print("\n RESULTADO ")

for est in estudiantes:
    print(f"{est['nombre']} -> {round(est['nota_final'],2)} -> ({est['clasificacion']})")
    
    promedio_grupo = suma_notas /
    len(estudiantes)
    
    print("\n RESUMEN DEL MODULO")
    print("Modulo:", modulos)
    print("coders resguistrados:", len(estudiantes))
    print("Promedio general:" , round(promedio_grupo,2))
    
    print("\n CLASIFICACION DEL GRUPO")
    
    print("Reprobados:", reprobados)
    print("Regulares:", regulares)
    print("Excelentes:", excelentes)
    
    print("\n MEJOR CODER DEL GRUPO")
    print(mejor_coder,"-", round(mejor_nota,2))
