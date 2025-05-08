# Diccionario de tasas de cambio respecto al USD
tasas_cambio = {
    "USD": 1.0,
    "EUR": 0.9,
    "COP": 4200,
}

# Función para convertir monedas
def convertir_divisa(monto, divisa_origen, divisa_destino):
    # Convertimos primero el monto a dólares
    monto_usd = monto / tasas_cambio[divisa_origen]
    # Luego a la moneda destino
    convertido = monto_usd * tasas_cambio[divisa_destino]
    return round(convertido, 2)

# Bloque principal con manejo de excepciones
try:
    # Pedir e intentar convertir el monto
    monto = float(input("Monto a convertir: "))
    
    # Verificar que el monto no sea negativo
    if monto <= 0:
        raise ValueError("El monto no puede ser negativo ni 0.")
   
    # Ingresar divisa origen y validar
    origen = input("Divisa origen (USD, EUR, COP): ").upper()
    if origen not in tasas_cambio:
        raise ValueError(f"Divisa origen no válida: {origen}")

    # Ingresar divisa destino y validar
    destino = input("Divisa destino (USD, EUR, COP): ").upper()
    if destino not in tasas_cambio:
        raise ValueError(f"Divisa destino no válida: {destino}")

    # Realizar conversión
    resultado = convertir_divisa(monto, origen, destino)
    print(f"{monto} {origen} son {resultado} {destino}")

except ValueError as e:
    print(f"Error: {e}")

finally:
    print("Proceso de conversión finalizado.")
