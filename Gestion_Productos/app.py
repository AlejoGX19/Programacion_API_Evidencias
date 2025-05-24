from fastapi import FastAPI, Request, Form # para recibir datos del formulario
from fastapi.responses import HTMLResponse, RedirectResponse # para redireccionar
from fastapi.staticfiles import StaticFiles # para servir archivos estáticos
from fastapi.templating import Jinja2Templates # para renderizar HTML
from starlette.status import HTTP_302_FOUND # para redireccionar
from modulos.db import get_connection # para la conexión a la base de datos
from descuento import aplicar_descuento # para aplicar el descuento

app = FastAPI()

# Servir archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Directorio de plantillas
templates = Jinja2Templates(directory="templates")

# Hashear contraseñas
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@app.get("/login", response_class=HTMLResponse)
async def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "error": None})

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, correo: str = Form(...), password: str = Form(...)):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
    usuario = cursor.fetchone()
    conn.close()
    return productos

@app.get("/register", response_class=HTMLResponse)
async def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "error": None})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, nombre: str = Form(...), telefono: str = Form(...), correo: str = Form(...), password: str = Form(...)):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuario WHERE correo = %s", (correo,))
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            return templates.TemplateResponse("register.html", {"request": request, "error": "El correo ya está registrado"})

        cursor.execute("INSERT INTO usuario (nombre, telefono, correo, password) VALUES (%s, %s, %s, %s)",
                       (nombre, telefono, correo, hash_password(password)))
        conn.commit()
        conn.close()
        return RedirectResponse(url="/login", status_code=HTTP_302_FOUND)
    except Exception as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": str(e)})

@app.get("/logout")
async def logout():
    response = RedirectResponse(url="/login", status_code=HTTP_302_FOUND)
    response.delete_cookie("usuario_logueado")
    return response

@app.get("/", response_class=HTMLResponse)
async def form_index(request: Request):
    usuario = request.cookies.get("usuario_logueado")
    if not usuario:
        return RedirectResponse(url="/login", status_code=HTTP_302_FOUND)

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
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    conn.close()
    return productos
