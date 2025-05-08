#------------------------- EXCEPCIONES-----------------------------

# Existen 3 tipos de sentencias de exepciones TRY | EXEPT | FYNALLY

# Inicio de sesion
usuarios = {
    "admin": "1234",
    "Alejo": "4321"
}

def iniciar_sesion():
    try:
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")

        if usuario not in usuarios: # se evalua si el usurio existe dentro del diccionario
            raise ValueError("El usuario no existe.") # ValueError la función recibió un argumento del tipo correcto pero con un valor inapropiado. || raise se utiliza para generar una excepción manual

        if usuarios[usuario] != contraseña: # se accede al valor asosciado al usuario y se compara
            raise ValueError("Contraseña incorrecta.")

    except ValueError as error:                     # si ocurre un excepcion el except se ejcutara mostrando el error 
        print(f"Error de autenticación: {error}")

    else:                                   # esto solo se ejcita si no ocurrio ninguna excepcion
        print(f"Bienvenido, {usuario}.")

    finally:
        print("Fin del intento de inicio de sesión.\n") # esto es lo ultimo que se ejecuta y siempre 

iniciar_sesion()


#------------------------ VALIDACIONES-----------------------------

# Formulario
def validar_nombre(nombre):
    if not nombre: # verifica que el nombre no se vacia
        raise ValueError("El nombre no puede estar vacío.")
    if not nombre.isalpha(): # .isalpha() verifica que la variable contenga letras del alfabeto
        raise ValueError("El nombre solo debe contener letras.")
    return nombre

def validar_edad(edad):
    edad = int(edad) # convierte la cadena a entero
    if edad <= 0: # verifica que la edad sea mayor a 0
        raise ValueError("La edad debe ser mayor que cero.")
    return edad

def validar_correo(correo):
    # "@" not in correo: verifica que contenga el @
    #"." not in correo.split("@")[-1] divide la cadena en el @ el -1 para acceder a la parte despues del @ y verifica el el "." este presente
    if "@" not in correo or "." not in correo.split("@")[-1]:
        raise ValueError("Correo electrónico inválido.")
    return correo

def validar_contraseña(contraseña):
    if len(contraseña) < 6: # Esta línea verifica si la longitud de la cadena e menor a 6
        raise ValueError("La contraseña debe tener al menos 6 caracteres.")
    return contraseña


def formulario():
    try:
        nombre = validar_nombre(input("Nombre: ").strip()) #.strip(): Elimina cualquier espacio en blanco al principio y al final de la cadena
        edad = validar_edad(input("Edad: ").strip())
        correo = validar_correo(input("Correo electrónico: ").strip())
        contraseña = validar_contraseña(input("Contraseña: ").strip())

    except ValueError as error:
        print(f"❌ Error: {error}")
    else:
        print("\n✅ Formulario completado con éxito:")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"Correo: {correo}")
    finally:
        print("Fin del proceso.\n")

formulario()
