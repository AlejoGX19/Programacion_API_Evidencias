#"Desarrollar una herramienta que valide automáticamente datos recogidos durante censos comunitarios 
# o encuestas sociales. Detecta errores comunes como edad inválida, campos vacíos, 
# formatos incorrectos en números o direcciones. Utiliza `try-except` 
# y validaciones lógicas para asegurar la calidad de la información recolectada.
# Sistema que recoge y valida entradas de encuestas (números, edades, direcciones)
import re



def validar_nombre(nombre):
    if not nombre:
        raise ValueError("El nombre no puede estar vacío.")
    if not nombre.replace(" ", "").isalpha():
        raise ValueError("El nombre solo debe contener letras.")
    return nombre

def validar_edad(edad):
    edad = int(edad)
    if edad <= 0 or edad > 110:
        raise ValueError("La edad debe ser un número válido entre 1 y 110.")
    return edad

def validar_correo(correo):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(patron, correo):
        print(f"Correo '{correo}' válido.")
        return correo

def validar_contraseña(contraseña):
    if len(contraseña) < 6:
        raise ValueError("La contraseña debe tener al menos 6 caracteres.")
    return contraseña

def validar_numero_hijos(hijos):
    hijos = int(hijos)
    if hijos < 0:
        raise ValueError("El número de hijos no puede ser negativo.")
    return hijos

def validar_direccion(direccion):
    if not direccion or len(direccion) < 5:
        raise ValueError("La dirección debe tener al menos 5 caracteres.")
    return direccion

def validar_telefono(telefono):
    if not telefono.isdigit() or len(telefono) < 10:
        raise ValueError("El número de teléfono debe contener 10 digitos numericos.")
    return telefono


def formulario_censo():
    try:
        print("Ingreso de datos para encuesta comunitaria\n")
        nombre = validar_nombre(input("Nombre completo: ").strip())
        edad = validar_edad(input("Edad: ").strip())
        correo = validar_correo(input("Correo electrónico: ").strip())
        print("La contraseña debe tener como minimo 6 caracteres")
        contraseña = validar_contraseña(input("Contraseña: ").strip())
        hijos = validar_numero_hijos(input("Número de hijos: ").strip())
        print("La direccion debe tener almenos 5 caracteres")
        direccion = validar_direccion(input("Dirección: ").strip())
        print("Ingrese un numero valido de 10 digitos.")
        telefono = validar_telefono(input("Teléfono: ").strip())
    except ValueError as error:
        print(f"\nError: {error}")
    else:
        print("\nFormulario de censo completado con éxito:")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Correo: {correo}")
        print(f"Hijos: {hijos}")
        print(f"Dirección: {direccion}")
        print(f"Teléfono: {telefono}")
    finally:
        print("Fin del proceso de validación.\n")


formulario_censo()