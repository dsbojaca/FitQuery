from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from backend.models import Base
from backend.database import engine
from backend.routes.fitquery_routes import router  # Rutas del backend

app = FastAPI()

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Configurar CORS para permitir llamadas desde GitHub Pages
origins = [
    "https://dsbojaca.github.io/FitQuery",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas del backend
app.include_router(router)

# Ruta absoluta a la carpeta "docs" (frontend estático)
FRONT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")

# Servir la carpeta completa para CSS y JS (si decides usar backend para frontend)
app.mount("/static", StaticFiles(directory=FRONT_DIR), name="static")

# Ruta para mostrar el HTML principal (si usas backend para frontend)
@app.get("/inicio")
def inicio():
    return FileResponse(os.path.join(FRONT_DIR, "index.html"))

# Ruta raíz redirecciona a /inicio (evitar 404 en /)
from fastapi.responses import RedirectResponse

@app.get("/")
def root():
    return RedirectResponse(url="/inicio")