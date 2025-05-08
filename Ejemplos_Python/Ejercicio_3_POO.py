# Crear una clase "Rectángulo" con métodos para calcular área y perímetro.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        area = self.base * self.altura
        return area

    def perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro


print("Bienvenido!")
print("Esta Ejercicio te calculara el area y el perimetro de un rectangulo segun las medidas que ingreses")
r_base = int(input("Ingresa cuanto mide la BASE del rectangulo en cm: "))
r_altura = int(input("Ingresa cuanto mide la ALTURA del rectangulo en cm: "))

rectangulo = Retangulo(r_base, r_altura)
area = rectangulo.area()
perimetro = rectangulo.perimetro()

print(f"El area del rectangulo es : {area} cm²")
print(f"El perimetro del rectangulo es : {perimetro} cm")