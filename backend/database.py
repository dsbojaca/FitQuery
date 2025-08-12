from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv()

# Primero intentamos usar DATABASE_URL (producción en Render)
DATABASE_URL = os.getenv("DATABASE_URL")

# Si no existe, usamos las variables locales
if not DATABASE_URL:
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear motor de conexión
engine = create_engine(DATABASE_URL)

# Crear sesión
SessionLocal = sessionmaker(bind=engine)

# ✅ Esta función permite inyectar la sesión de la base de datos en los endpoints
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()