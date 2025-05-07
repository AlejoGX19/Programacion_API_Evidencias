# Programcion Orientada a Objetos (POO)

#- `class`: Define una clase. 
# - `__init__`: Método constructor. 
# - `self`: Referencia al objeto actual. 
# - `super()`: Llama al constructor de la clase padre. 
# - `__atributo`: Atributo privado.

print("---Clase y Objeto---")

# Clase y Objeto
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")
    
# Crear Objeto 
p1 = Persona("Alejandro", 19)
p1.saludar()        

print("---Encapsulamiento---")
# Encapsulamiento
class CunetaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self. __saldo = saldo #atributo privado

    def mostrar_saldo(self):
        print(f"Saldo de {self.__titular}: ${self.__saldo}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

cuenta = CunetaBancaria("Alejo", 10000)
cuenta.depositar(5000)
cuenta.mostrar_saldo()
# print(cuenta.__saldo) esto da error

print("---Herencia---")
# Herencia
class Empleado(Persona):
    def __init__(self, nombre, edad, cargo):
        super().__init__(nombre, edad)
        self.cargo = cargo
    
    def presentar(self):
        print(f"{self.nombre}, {self.edad} años, trabaja como {self.cargo}")
    
emp = Empleado("Alejandro", 19, "Desarrollador")
emp.presentar()

print("---Polimorfismo---")
# Polimorfismo
class Animal: 
    def hablar(self):
        print("El animal hace un sonido")
    
class Perro(Animal):
    def hablar(self):
        print("El perro dice: Guau!")

class Gato(Animal):
    def hablar(self):
        print("El gato dice: Miau!")

animales = [Animal(), Perro(), Gato()]

for animal  in animales:
    animal.hablar()

print("---Integrador---")
# Ejemplo de Integrador
class Producto :
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar(self):
        print(f"{self.nombre} cuesta ${self.precio}")
    
class CarritoCompras:
    def __init__(self):
        self.productos = []
    
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_carrito(self):
        print("Carrito de Compras")
        for prod in self.productos:
             prod.mostrar()

# Uso
p1 = Producto("Laptop", 3000)

p2 = Producto("Mouse", 150)

carrito = CarritoCompras()

carrito.agregar_producto(p1)

carrito.agregar_producto(p2)

carrito.mostrar_carrito()