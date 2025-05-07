# 1 crear un programa que pida al usuario su nombre y edad y le diga si puede votar (major de 18 años)

print("Bienvenido!! ")
print("Digita tu nombre y edad para verificar si puede votar")
nombre = (input("Ingresa tu nombre: "))
edad = int(input("Ingresa tu edad: "))
if edad >= 18:
    print(f"{nombre} Puedes votar ")
else:
    print(f"{nombre} No puedes votar ")