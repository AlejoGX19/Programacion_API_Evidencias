from datetime import datetime

## ClASE PRODUCTO (Encapsulamiento y Abstracción)
class Producto:

    ## COSTRUCTOR 
    def __init__(self, identificador, nombre, descripcion, precio, cantidad_disponible):## SELF hace refencia la instacia del objeto 
        ## PARAMETROS
        self.identificador = identificador
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible
        self.fecha_creacion = datetime.now()
        self.fecha_modificacion = None

    ## METODO DE LA CLASE PRODUCTO
    def actualizar_producto(self, nombre=None, descripcion=None, precio=None, cantidad_disponible=None):
        if nombre is not None:
            self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        if cantidad_disponible is not None:
            self.cantidad_disponible = cantidad_disponible
        self.fecha_modificacion = datetime.now()

    ## METODO DE LA CLASE PRODUCTO DE COMO REPRESENTAR EL OBJETO (Polimorfismo)
    def __str__(self):
        return f"ID: {self.identificador}\nNombre: {self.nombre}\nDescripción: {self.descripcion}\nPrecio: ${self.precio:.2f}\nCantidad: {self.cantidad_disponible}\nCreado el: {self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S')}\nModificado el: {self.fecha_modificacion.strftime('%Y-%m-%d %H:%M:%S') if self.fecha_modificacion else 'Sin modificaciones'}"

## CLASE DE GESTOR DE INVENTARIO
class GestorInventario:

    ## COSTRUCTOR INICIALIZA LOS ATRIBUTOS DE LA INSTANCIA 
    def __init__(self):
        self.inventario = {}
        self.siguiente_id = 1  # Para generar identificadores únicos automáticamente

    ## METODO PARA CREAR PRODUCTO 
    def crear_producto(self, nombre, descripcion, precio, cantidad_disponible):
        identificador = self.siguiente_id
        nuevo_producto = Producto(identificador, nombre, descripcion, precio, cantidad_disponible)
        self.inventario[identificador] = nuevo_producto
        self.siguiente_id += 1
        print(f"Producto '{nuevo_producto.nombre}' (ID: {nuevo_producto.identificador}) creado exitosamente.")

    ## METODO PARA BUSCAR PRODUCTOS 
    def leer_producto(self, identificador):
        if identificador in self.inventario:
            return self.inventario[identificador]
        else:
            print(f"No se encontró ningún producto con el ID: {identificador}")
            return None
        
    ## METODO PARA ACTUALIZAR PRODUCTO
    def actualizar_producto(self, identificador, nombre=None, descripcion=None, precio=None, cantidad_disponible=None):
        producto = self.leer_producto(identificador)
        if producto:
            producto.actualizar_producto(nombre, descripcion, precio, cantidad_disponible)
            print(f"Producto '{producto.nombre}' (ID: {producto.identificador}) actualizado exitosamente.")

    ## METODO PARA ELIMINAR PRODUCTO
    def borrar_producto(self, identificador):
        if identificador in self.inventario:
            producto_eliminado = self.inventario.pop(identificador)
            print(f"Producto '{producto_eliminado.nombre}' (ID: {producto_eliminado.identificador}) eliminado exitosamente.")
        else:
            print(f"No se encontró ningún producto con el ID: {identificador}")

    ## METODO PARA LISTAR PRODUCTO
    def listar_productos(self):
        ## Verifica si hay productos o no
        if self.inventario:
            print("\n--- Inventario de Productos ---")
            for identificador, producto in self.inventario.items():
                print(f"ID: {identificador}, {producto.nombre} - Cantidad: {producto.cantidad_disponible}, Precio: ${producto.precio:.2f}")
            print("-----------------------------\n")
        else:
            print("El inventario está vacío.")

## INTERFAS DE USUARIO (Abstracción)
def menu_inventario():
    gestor = GestorInventario() ## Se cre una instancia a la clase 

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Leer producto")
        print("4. Actualizar producto")
        print("5. Borrar producto")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            descripcion = input("Ingrese la descripción del producto: ")
            try:
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad disponible: "))
                gestor.crear_producto(nombre, descripcion, precio, cantidad)
            except ValueError:
                print("Por favor, ingrese valores numéricos válidos para precio y cantidad.")
        elif opcion == '2':
            gestor.listar_productos()
        elif opcion == '3':
            try:
                identificador = int(input("Ingrese el ID del producto a leer: "))
                producto = gestor.leer_producto(identificador)
                if producto:
                    print(producto) # (Polimorfismo): Se utiliza el método __str__ de la clase Producto para mostrar la información
            except ValueError:
                print("Por favor, ingrese un número válido para el ID.")
        elif opcion == '4':
            try:
                identificador = int(input("Ingrese el ID del producto a actualizar: "))
                producto = gestor.leer_producto(identificador)
                if producto:
                    nuevo_nombre = input(f"Nuevo nombre (dejar en blanco para no cambiar): ") or None
                    nueva_descripcion = input(f"Nueva descripción (dejar en blanco para no cambiar): ") or None
                    nuevo_precio_str = input(f"Nuevo precio (dejar en blanco para no cambiar): ")
                    nuevo_precio = float(nuevo_precio_str) if nuevo_precio_str else None
                    nueva_cantidad_str = input(f"Nueva cantidad disponible (dejar en blanco para no cambiar): ")
                    nueva_cantidad = int(nueva_cantidad_str) if nueva_cantidad_str else None
                    gestor.actualizar_producto(identificador, nuevo_nombre, nueva_descripcion, nuevo_precio, nueva_cantidad)
            except ValueError:
                print("Por favor, ingrese un número válido para el ID, precio o cantidad.")
        elif opcion == '5':
            try:
                identificador = int(input("Ingrese el ID del producto a borrar: "))
                gestor.borrar_producto(identificador)
            except ValueError:
                print("Por favor, ingrese un número válido para el ID.")
        elif opcion == '6':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_inventario()