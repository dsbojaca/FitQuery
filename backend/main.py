from fastapi import FastAPI
from models import Base
from database import engine
from routes.fitquery_routes import router  # Asegúrate de que el path es correcto

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir rutas
app.include_router(router)