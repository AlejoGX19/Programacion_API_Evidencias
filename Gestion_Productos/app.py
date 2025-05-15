from flask import Flask, render_template, request
from descuento import aplicar_descuento
import mysql.connector

app = Flask(__name__)

def obtener_productos():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='descuentos'
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT nombre, precio_inicial FROM producto")
    productos = cursor.fetchall()
    conn.close()
    return productos


@app.route('/', methods=['GET', 'POST'])
def index():
    productos = obtener_productos()
    resultado = error = None
    producto_seleccionado = ""

    if request.method == 'POST':
        try:
            producto_seleccionado = request.form['producto']
            descuento = float(request.form['descuento'])

            # Buscar el producto por nombre
            producto = next((p for p in productos if p['nombre'] == producto_seleccionado), None)
            if producto is None:
                raise ValueError("Producto no encontrado.")
            
            precio = producto['precio_inicial']
            resultado = aplicar_descuento(precio, descuento)

            # Guardar el precio final en la base de datos
            conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='descuentos'
            )
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE producto SET precio_final = %s WHERE nombre = %s",
                (resultado, producto_seleccionado)
            )
            conexion.commit()
            cursor.close()
            conexion.close()

        except ValueError as ve:
            error = str(ve)
        except Exception as e:
            error = f"Ocurrió un error inesperado: {str(e)}"

    return render_template(
        'index.html',
        productos=productos,
        resultado=resultado,
        error=error,
        seleccionado=producto_seleccionado
    )

if __name__ == '__main__':
    app.run(debug=True)
