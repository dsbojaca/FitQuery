from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from sqlalchemy import text
from sqlalchemy.orm import Session

from backend.models import Base
from backend.database import engine, get_db
from backend.routes.fitquery_routes import router
from backend.routes.auth_routes import router as auth_router
from backend.auth import get_current_user  # 🔑 Importar función de auth

app = FastAPI()

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# Configurar CORS para permitir llamadas desde local y GitHub Pages
origins = [
    "http://localhost:8000",   # para pruebas locales
    "http://127.0.0.1:8000",   # para pruebas locales
    "https://dsbojaca.github.io",  # producción en GitHub Pages
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
app.include_router(auth_router, prefix="/auth", tags=["auth"])

# Ruta absoluta a la carpeta "docs" (frontend estático)
FRONT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs")

# Servir estáticos (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory=FRONT_DIR), name="static")

# Rutas para mostrar HTMLs
@app.get("/inicio")
def inicio(current_user: dict = Depends(get_current_user)):  # 🔒 Protegida
    return FileResponse(os.path.join(FRONT_DIR, "index.html"))

@app.get("/auth-page")
def auth_page():
    return FileResponse(os.path.join(FRONT_DIR, "auth.html"))

@app.get("/")
def root():
    return RedirectResponse(url="/auth-page")

# Ruta de testeo de la DB
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM fit_schema.usuarios LIMIT 5"))
    return result.fetchall()