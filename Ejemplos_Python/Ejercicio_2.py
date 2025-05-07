# Simula un cajero automatico que permita al usuario retirar dinero hasta que no tenga saldo
print("Bienvenido!! ")
print("Este algoritmo te permitira retirar dinero hasta que el cajero se quede sin dinero! ")

usuario = input("Por favor ingrese su nombre de usuario: ")
saldo = 100000
clave = int(input("Ingresa tu clave de 4 dígitos: "))

clave_valida = 1234

if clave == clave_valida:
    while True:
        print(f"Saldo actual: {saldo}")
        retiro = int(input("Ingresa la cantidad que deseas retirar: "))
        
        if retiro <= saldo:
            saldo -= retiro 
            print(f"Retiro exitoso. Saldo restante: {saldo}")
            
            if saldo == 0:
                print(f" {usuario} Has agotado tu saldo. Gracias por usar BancoAlejo!")
                break
        else:
            print("No tienes la cantidad suficiente")
else:
    print("Clave incorrecta")