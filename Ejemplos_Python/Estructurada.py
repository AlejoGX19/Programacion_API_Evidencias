from datetime import date, datetime, timedelta

print("Hola mundo desde el archivo estructurada.py")

# Manejo de variables
nombre = "Alejo"
edad = 19
estatura = 1.75
print(f"{nombre} tiene {edad} años y mide {estatura} metros.")

# Conversion de tipos
edad_str = "19"
edad_int = int(edad_str)
print(edad_int + 5)

# Manjeo de fechas
fecha_hoy = date.today()
fecha_hora_actual = datetime.now()
cumpleaños = date(2005, 7, 6)
mañana = date.today() + timedelta(days=1)
dias_trancurridos = (fecha_hoy - date(2025, 1, 1)).days
print(dias_trancurridos)

# Manejo de booleans y estructra if-else con and
es_mayor_de_edad = True
tiene_licencia = False
if es_mayor_de_edad and tiene_licencia:
    print("Puede conducir.")
else:
    print("No puede conducir.")

# Manejo de rangos con if-else
nota = 85
if nota >= 90:
    print("Excelenete")
elif nota >= 70:
    print("Aprovado")
else:
    print("Reprovado")

# Simulacion de casos
opcion = 2
if opcion == 1:
    print("Opcion 1")
elif opcion == 2:
    print("Opcion 2")
else:
    print("Opcion no valida")

# Simulacion de casos con diccionario
def opcion_1():
    return "Opcion 1"
def opcion_2():
    return "Opcion 2"
switch = {1: opcion_1, 2: opcion_2}
resultado = switch.get(1, lambda: "Opcion no valida")()
print(resultado)

# Bucles (for y while)

# Bucle for tradicional 
for i in range(1, 6):
    print(i)

print("----------")
# Bucle while tradicional
contador = 3
while contador > 0:
    print(contador)
    contador -= 1

# Simulacion de bucle do while
while True:
    numero = int(input("Ingrese un numero mayor que 0: "))
    if numero > 0:
        break

# Bucle tipo foreach con listas y diccionario
animales = ["gato", "perro", "loro"]
for animal in animales:
    print(animal)

persona = {"nombre": "Alejo", "edad": 19}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Listas y operaciones basicas
frutas = ["manzana", "banana", "pera"]
frutas.append("mango")
print(frutas[0]) # manzana ya que esta en pasicion 0 de la lista
print("--------")
for fruta in frutas:
    print(fruta)

## Funciones
def saludar(nombre):
    return f"Hola, {nombre}!"
print(saludar("Alejandro"))

## Funcion que suma dos numeros
def sumar(a, b):
    return a + b 
print(f"La suma es: {sumar(5, 7)}")

## Funcion que resta dos numeros
def restar(a, b):
    return a - b 
print(f"La resta es: {restar(5, 7)}")

## Funcion que multiplica dos numeros
def multiplicar(a, b):
    return a * b 
print(f"La multiplica es: {multiplicar(5, 7)}")

## Funcion que divide dos numeros
def dividir(a, b):
    return a / b 
print(f"La divicion es: {dividir(12, 4)}")

## Diccionarios
persona = {
    "nombre": "Alejandro",
    "edad":  19,
    "profesion": "Desarrollador"
}
print(persona["nombre"])
persona["ciudad"] = "Medellin"
print(persona)

## Integradores
personas = []
for i in range(3):
    nombre = input("Ingresa tu nombre: ") 
    edad = int(input("Ingresa tu edad: ")) 
    personas.append({"nombre": nombre, "edad": edad})

print("\nSaludos personalizados:") 
for persona in personas: 
    print(f"Hola {persona['nombre']}, tienes {persona['edad']} años.")