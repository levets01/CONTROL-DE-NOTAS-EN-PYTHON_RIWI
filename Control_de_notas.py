print("░█▀▀░▀█▀░█▀▀░▀█▀░█▀▀░█▄█░█▀█░░░█▀▄░█▀▀░░░█▀▀░█▀█░█▀█░▀█▀░█▀▄░█▀█░█░░░░░█▀▄░█▀▀░░░█▀█░█▀█░▀█▀░█▀█░█▀▀ ")
print("░▀▀█░░█░░▀▀█░░█░░█▀▀░█░█░█▀█░░░█░█░█▀▀░░░█░░░█░█░█░█░░█░░█▀▄░█░█░█░░░░░█░█░█▀▀░░░█░█░█░█░░█░░█▀█░▀▀█ ")
print("░▀▀▀░▀▀▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀░▀░░░▀▀░░▀▀▀░░░▀▀▀░▀▀▀░▀░▀░░▀░░▀░▀░▀▀▀░▀▀▀░░░▀▀░░▀▀▀░░░▀░▀░▀▀▀░░▀░░▀░▀░▀▀▀ ")

#aca esta la lista en la que se almacenan los estudiantes
estudiantes = []

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

    estudiante = {
                "nombre" : nombre,
                "nota_final" : nota_final

            }
    estudiantes.append(estudiante) 
    
    
print ("\n RESULTADOS")

for est in estudiantes:
    if est ["nota_final"] < 50:
        
        print(f"MODULO{modulos} va perdiendo ")

        print(f"""{est['nombre']} -> 
              {round(est['nota_final'],2)} va perdiendo""")
            
    else:
          print(f"MODULO {modulos} Aprobado ")
          print(f"""{est['nombre']} -> 
              {round(est['nota_final'],2)} Aprobó""")
