from fastapi import FastAPI, Request, Form # para recibir datos del formulario
from fastapi.responses import HTMLResponse, RedirectResponse # para redireccionar
from fastapi.staticfiles import StaticFiles # para servir archivos estáticos
from fastapi.templating import Jinja2Templates # para renderizar HTML
from starlette.status import HTTP_302_FOUND # para redireccionar
from modulos.db import get_connection # para la conexión a la base de datos
from descuento import aplicar_descuento # para aplicar el descuento

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static") # para servir archivos estáticos
templates = Jinja2Templates(directory="templates")

# Función para obtener la lista de productos
def obtener_productos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    conn.close()
    return productos

@app.get("/", response_class=HTMLResponse) # muestar la vista principal index.html
async def form_index(request: Request):
    productos = obtener_productos()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "productos": productos,
        "resultado": None,
        "error": None,
        "seleccionado": ""
    })

@app.post("/", response_class=HTMLResponse)
async def calcular_descuento(request: Request, producto: str = Form(...), descuento: float = Form(...)):
    productos = obtener_productos()
    resultado = error = None

    try:
        seleccionado = next((p for p in productos if p["nombre"] == producto), None)
        if not seleccionado:
            raise ValueError("Producto no encontrado")

        precio = seleccionado["precio_inicial"]
        resultado = aplicar_descuento(precio, descuento)

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE producto SET precio_final = %s WHERE nombre = %s",
            (resultado, producto)
        )
        conn.commit()
        conn.close()
    except Exception as e:
        error = str(e)
        seleccionado = producto
        resultado = None

    return templates.TemplateResponse("index.html", {
        "request": request,
        "productos": productos,
        "resultado": resultado,
        "error": error,
        "seleccionado": producto
    })

@app.get("/productos", response_class=HTMLResponse) # lista los productos
def listar_productos(request: Request):
    productos = obtener_productos()
    return templates.TemplateResponse("productos.html", {"request": request, "productos": productos})

@app.post("/productos/agregar", response_class=HTMLResponse) # agrega un producto
def agregar_producto(request: Request, nombre: str = Form(...), precio_inicial: int = Form(...)):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO producto (nombre, precio_inicial) VALUES (%s, %s)",
        (nombre, precio_inicial)
    )
    conn.commit()
    conn.close()
    return RedirectResponse(url="/productos", status_code=HTTP_302_FOUND)

@app.get("/productos/editar/{id}", response_class=HTMLResponse) # muestra formulario de edición
def editar_form(request: Request, id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto WHERE id = %s", (id,))
    producto = cursor.fetchone()
    conn.close()
    return templates.TemplateResponse("editar.html", {"request": request, "producto": producto})

@app.post("/productos/editar/{id}", response_class=HTMLResponse) # edita un producto
def editar_producto(id: int, nombre: str = Form(...), precio_inicial: int = Form(...)):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE producto SET nombre = %s, precio_inicial = %s WHERE id = %s",
        (nombre, precio_inicial, id)
    )
    conn.commit()
    conn.close()
    return RedirectResponse(url="/productos", status_code=HTTP_302_FOUND)

@app.get("/productos/eliminar/{id}", response_class=HTMLResponse) # elimina un producto
def eliminar_producto(id: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM producto WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return RedirectResponse(url="/productos", status_code=HTTP_302_FOUND)
