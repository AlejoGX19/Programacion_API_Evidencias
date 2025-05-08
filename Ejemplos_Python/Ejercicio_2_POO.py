# Crear una clase `Estudiante` que herede de "Persona" y tenga un atributo "carrera".

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def presentarse(self):
        print(f"Hola! mi nombre es {self.nombre}, tengo {self.edad} y estoy haciendo la carrera de {self.carrera}")

estu = Estudiante("Alejandro", 19, "Analisis y Desarrollo de Software")
estu.presentarse()