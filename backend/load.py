import requests
from dotenv import load_dotenv
import os

from models import Ejercicio, Base
from database import engine, SessionLocal

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

# URL de la API externa
API_URL = "https://api.api-ninjas.com/v1/exercises"
MUSCULOS = ["chest", "back", "biceps", "triceps", "legs", "shoulders", "abdominals"]

def fetch_exercises():
    all_exercises = []
    for muscle in MUSCULOS:
        params = {"muscle": muscle}
        headers = {"X-Api-Key": API_KEY}
        try:
            response = requests.get(API_URL, headers=headers, params=params)
            response.raise_for_status()
            all_exercises.extend(response.json())
        except Exception as e:
            print(f"❌ Error al obtener ejercicios de {muscle}: {e}")
    return all_exercises

def insert_exercises(exercises):
    db = SessionLocal()
    inserted = 0
    try:
        for ex in exercises:
            nombre = ex.get("name", "Desconocido")
            grupo = ex.get("muscle", "Otro")
            equipo = ex.get("equipment", "Sin equipo")
            dificultad = ex.get("difficulty", "Media")
            instrucciones = ex.get("instructions", "")

            # Verificar si ya existe un ejercicio con ese nombre
            exists = db.query(Ejercicio).filter_by(nombre=nombre).first()
            if exists:
                continue

            ejercicio = Ejercicio(
                nombre=nombre,
                grupo_muscular=grupo,
                equipo=equipo,
                dificultad=dificultad,
                instrucciones=instrucciones
            )
            db.add(ejercicio)
            inserted += 1

        db.commit()
        print(f"✅ {inserted} ejercicios insertados con éxito.")
    except Exception as e:
        db.rollback()
        print("❌ Error durante la inserción:", e)
    finally:
        db.close()

# Programa principal
if __name__ == "__main__":
    print("📡 Obteniendo ejercicios desde API...")
    ejercicios = fetch_exercises()
    insert_exercises(ejercicios)