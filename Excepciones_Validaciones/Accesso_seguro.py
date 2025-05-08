# Ejercicio 2: Acceso seguro a elementos de una lista con manejo de IndexError

def obtener_elemento_lista(mi_lista, indice):
    try:
        elemento = mi_lista[indice]  # Intenta acceder al elemento
        print(f"Elemento en índice {indice}: {elemento}")
        return elemento
    except IndexError:  # Si el índice está fuera de rango
        print(f"¡Error! Índice {indice} fuera de rango (tamaño: {len(mi_lista)}).")
        return None

mi_lista_ejemplo = [10, 20, 30, 40, 50]
obtener_elemento_lista(mi_lista_ejemplo, 2)
obtener_elemento_lista(mi_lista_ejemplo, 5)
obtener_elemento_lista(mi_lista_ejemplo, -1)