import unittest #Modulo de pruebas integrado de python
from descuento import aplicar_descuento

class TestDescuento(unittest.TestCase):
    
    #PRUEBA 1
    def test_descuento_correcto(self): #Referencia al objeto actual de una clase para acceder a sus propios metodos y atributos
        self.assertEqual(aplicar_descuento(100, 10), 90.00) #Compara el resultado real con el esperado, si son iguales pasará la prueba
        self.assertEqual(aplicar_descuento(200, 25), 150.00)

    #PRUEBA 2
    def test_porcentaje_invalido(self):
        try:
            aplicar_descuento(100, 50)
        except ValueError as e:
            print(f"Error en test_porcentaje_invalido: {e}")
            self.fail(f"Error: {e}")

        try:
            aplicar_descuento(100, 50)
        except ValueError as e:
            print(f"Error en test_porcentaje_invalido: {e}")
            self.fail(f"Error: {e}")

    #PRUEBA 3
    def test_precio_negativo(self):
        try:
            aplicar_descuento(50, 10)
        except ValueError as e:
            print(f"Error en test_precio_negativo: {e}")
            self.fail(f"Error: {e}")

#Para correr todas del archivo directamente
if __name__ == '__main__':
    unittest.main()

#Comando para ejecutar pruebas: python -m unittest discover -s testing -p "pruebas_*.py" recorre el directorio de testing y busca archivos que empiecen con pruebas y terminen con .py