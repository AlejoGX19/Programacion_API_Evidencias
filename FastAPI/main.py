from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
#from typing import Dict #permite definir el tipo de un diccionario
import mysql.connector

# http://localhost:8000/docs documentacion de Swagger
# http://localhost:8000/redoc documentacion de ReDoc

app = FastAPI()

#Configiracion de conexcion de coneccion Mysql
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'fastapi_db'
}

# Modelo Pydantic 
# class Persona(BaseModel):
#     nombre: str
#     edad: int
#     estatura: float
#     estado: bool 

#personas_db: Dict[str, Persona] = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.get("/saludo/{nombre}")
# def saludar(nombre: str):
#     return {"mensaje": f"Hola {nombre}, bienvenido a FastAPI!"}


# @app.post("/crear-persona/")
# def crear_persona(persona: Persona):
#     if persona.nombre in personas_db:
#         return {"mensaje": f"La persona {persona.nombre} ya existe."}
    
#     persona.estado = "Vivo" if persona.estado else "Muerto"
#     personas_db[persona.nombre] = persona 
#     return {"mensaje": f"Persona {persona.nombre} creada con éxito! Estatura: {persona.estatura} y estado: {persona.estado}"}

# @app.put("/actualizar-persona/")
# def actualizar_persona( persona: Persona):
#     if persona.nombre not in personas_db:
#         return {"mensaje": f"La persona {persona.nombre} no existe."}
    
#     persona.estado = "Vivo" if persona.estado else "Muerto"
#     personas_db[persona.nombre] = persona
#     return {"mensaje": f"Persona {persona.nombre} actualizada con éxito!"}

# @app.delete("/eliminar-persona/{nombre}")
# def eliminar_persona(nombre: str):
#     if nombre not in personas_db:
#         return {"mensaje": f"La persona {nombre} no existe."}
    
#     del personas_db[nombre]
#     return {"mensaje": f"Persona {nombre} eliminada con éxito!"}

# @app.get("/personas/")
# def listar_personas():
#     return {"personas": list(personas_db.values())} 

#-------------------------------------------------------------------------------

class Persona(BaseModel):
    nombre: str
    edad: int

@app.post("/personas")
def crear_persona(persona: Persona):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO personas (nombre, edad) VALUES (%s, %s)", (persona.nombre, persona.edad, ))
    conn.commit()
    cursor.close()
    conn.close()
    return {"mensaje": f"Persona {persona.nombre} creada con éxito!"}

@app.get("/personas")
def listar_personas():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, edad FROM personas")
    personas = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"id": persona[0], "nombre": persona[1], "edad": persona[2]} for persona in personas]


@app.get("/personas/{persona_id}")
def obtener_persona(persona_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, nombre, edad FROM personas WHERE id = %s", (persona_id,))
    persona = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if persona:
        return {"id": persona[0], "nombre": persona[1], "edad": persona[2]}
    else:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
@app.put("/personas/{persona_id}")
def actualizar_persona(persona_id: int, persona: Persona):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("UPDATE personas SET nombre = %s, edad = %s WHERE id = %s", (persona.nombre, persona.edad, persona_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    return {"mensaje": f"Persona {persona.nombre} actualizada con éxito!"}

@app.delete("/personas/{persona_id}")
def eliminar_persona(persona_id: int):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM personas WHERE id = %s", (persona_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Persona no encontrada")
    
    return {"mensaje": f"Persona con ID {persona_id} eliminada con éxito!"}