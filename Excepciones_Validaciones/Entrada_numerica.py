
# Ejercicio 1: Validación de entrada numérica con manejo de ValueError

def ingresar_edad():
    while True:
        try:
            edad_str = input("Por favor, ingresa tu edad: ")
            edad = int(edad_str)  # Intenta convertir a entero
            if edad <= 0:
                print("La edad debe ser un número positivo.")
            else:
                print(f"Tu edad es: {edad} años.")
                return edad  # Devuelve la edad válida
        except ValueError:  # Si la conversión falla
            print("¡Error! Entrada no válida. Intenta de nuevo.")

ingresar_edad()


