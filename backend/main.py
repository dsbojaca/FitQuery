from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from models import Base
from database import engine
from routes.fitquery_routes import router  # Rutas del backend

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir rutas del backend
app.include_router(router)

# Ruta absoluta a la carpeta "front"
FRONT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "frontend")

# Servir la carpeta completa para CSS y JS
app.mount("/static", StaticFiles(directory=FRONT_DIR), name="static")

# Ruta para mostrar el HTML
@app.get("/inicio")
def inicio():
    return FileResponse(os.path.join(FRONT_DIR, "index.html"))