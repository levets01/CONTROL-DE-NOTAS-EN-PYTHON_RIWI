#heladeria
vainilla = 0
chocolate = 0
fresa = 0

for i in range (1,6):
    print(f"pedido {i}:")
    sabor = input("Ingrese el sabor (Vainilla,Cholote,Fresa: )").lower
    
    #aca de hara la condicion de contar los sabores pedidos 
    
    if sabor == "vainilla":
        vainilla +=1
        
    elif sabor == "chocolate":
        chocolate +=1
    elif sabor == "fresa":
        fresa +=1
        
    else:
        print("Sabor no valido. Intente nuevamente")
        
        print("\n==== RESUMEN DE PEDIDOS ====")
        print(f"Vainilla:{vainilla}")
        print(f"Chocoloate:{chocolate}")
        print(f"fresa:{fresa}")
