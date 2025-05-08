# Crear una clase "Libro" con titulo, autor, año y un metodo para mostrar sus datos

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año

    def mostrarLibro(self):
        print(f"Este es el libro se llama {self.titulo} y fue escrito por {self.autor} y salio en el año {self.año}")

libro = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez", 1967)
libro.mostrarLibro()