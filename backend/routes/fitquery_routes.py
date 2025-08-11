from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.database import get_db
from backend.models import Ejercicio
from backend.schemas import EjercicioSchema

router = APIRouter()

@router.get("/ejercicios", response_model=List[EjercicioSchema])
def get_ejercicios(
    nombre: Optional[str] = Query(None),
    grupo_muscular: Optional[str] = Query(None),
    dificultad: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    print("👉 Filtros recibidos:", nombre, grupo_muscular, dificultad)

    query = db.query(Ejercicio)

    if nombre:
        nombre = nombre.strip()
        query = query.filter(Ejercicio.nombre.ilike(f"%{nombre}%"))
    
    if grupo_muscular:
        grupo_muscular = grupo_muscular.strip()
        query = query.filter(Ejercicio.grupo_muscular.ilike(f"%{grupo_muscular}%"))
    
    if dificultad:
        dificultad = dificultad.strip()
        query = query.filter(Ejercicio.dificultad.ilike(f"%{dificultad}%"))

    return query.all()
