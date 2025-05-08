# Ejercicio 3: Validación de formato de correo electrónico con expresiones regulares y manejo de excepciones personalizadas

import re

class FormatoCorreoInvalidoError(Exception):
    def _init_(self, mensaje):
        super()._init_(mensaje)

def validar_correo_electronico(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(patron, correo):  # Intenta hacer coincidir el patrón
        print(f"Correo '{correo}' válido.")
        return True
    else:
        raise FormatoCorreoInvalidoError(f"Correo '{correo}' inválido.")

correos_a_probar = ["usuario@dominio.com", "otro@sub.dominio.net", "invalido@", "@invalido.com", "sinpunto@com"]

for correo in correos_a_probar:
    try:
        validar_correo_electronico(correo)
    except FormatoCorreoInvalidoError as e:  # Captura la excepción personalizada
        print(f"¡Error! {e}")