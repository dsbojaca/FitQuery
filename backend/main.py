from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Base, Ejercicio


# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependencia para obtener sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Ruta GET para listar todos los ejercicios
@app.get("/ejercicios")
def listar_ejercicios(db: Session = Depends(get_db)):
    ejercicios = db.query(Ejercicio).all()
    return ejercicios
