from flask import Flask, render_template, request #Clase principal para crear la aplicación, request para acceder a los datos enviados desde el formulario 
from descuento import aplicar_descuento

app = Flask(__name__) #Creación de instancia de la aplicación Flask

# Diccionario de productos
productos = {
    "Camiseta": 50000,
    "Pantalón": 80000,
    "Zapatos": 100000
}

@app.route('/', methods=['GET', 'POST']) #Ruta principal con métodos get y post para cuando el usuario envía el formulario
def index():
    resultado = error = None #Guarda el precio con descuento y el error se mostrará en caso de excepciones
    producto_seleccionado = "" 
    if request.method == 'POST': #Si el usuario envía el formulario
        try:
            producto_seleccionado = request.form['producto']
            precio = productos[producto_seleccionado]
            descuento = float(request.form['descuento'])
            resultado = aplicar_descuento(precio, descuento)
    #Manejo de errores en caso de errores con la función o porcentajes inválidos
        except ValueError as ve:
            error = str(ve)
        except Exception:
            error = "Ocurrió un error inesperado."
    #Renderizado de la plantilla HTML, envia los datos mencionados
    return render_template('index.html', productos=productos, resultado=resultado, error=error, seleccionado=producto_seleccionado)

    #Arranque del servidor
if __name__ == '__main__':
    app.run(debug=True)
