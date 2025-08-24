from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# URL de conexión directa a PostgreSQL en Render
DATABASE_URL = os.getenv('DATABASE_URL')

# Crear motor de conexión con schema fit_schema
engine = create_engine(
    DATABASE_URL,
    connect_args={"options": "-c search_path=fit_schema"}
)

# Base para los modelos
Base = declarative_base()

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener la sesión
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()