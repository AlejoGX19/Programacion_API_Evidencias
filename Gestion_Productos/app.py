from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.status import HTTP_302_FOUND
from modulos.db import get_connection
from descuento import aplicar_descuento
import hashlib

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

    if usuario and usuario["password"] == hash_password(password):
        response = RedirectResponse(url="/", status_code=HTTP_302_FOUND)
        response.set_cookie(key="usuario_logueado", value=correo)
        return response
    elif usuario:
        return templates.TemplateResponse("login.html", {"request": request, "error": "Contraseña incorrecta"})
    else:
        return RedirectResponse(url="/register", status_code=HTTP_302_FOUND)

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

def obtener_productos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM producto")
    productos = cursor.fetchall()
    conn.close()
    return productos
