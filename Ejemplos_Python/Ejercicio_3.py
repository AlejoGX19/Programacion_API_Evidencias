# Crear un programa que almacene una lista de frutas y permita al usurio bucar si una fruta esta en la lista 

print("Bienvenido!! ")
print("Este algoritmo te permitira ingresar una lista de frutas y buscar en ella ")

frutas = [] 
while True:
    print("Que deceas hacer?")
    print("1- Ingresar una fruta")
    print("2- Buscar una fruta")
    print("3- Salir")
    opcion = int(input("Ingrese la opcion que deseas realizar: "))
    if opcion == 1:
        insert = input("Ingrese el nombre de la fruta: ")
        frutas.append(insert)
        print(f"'{insert}' ha sido agregada a la lista.")
    elif opcion == 2:
        buscar = input("Ingrese el nombre de la fruta a buscar: ")
        if buscar in frutas:
            print(f"¡'{buscar}' sí está en la lista de frutas!")
        else:
            print(f"Lo siento, '{buscar}' no se encuentra en la lista.")
    elif opcion == 3:
        break
    else:
        print("Ingrese un opcion valida!")
