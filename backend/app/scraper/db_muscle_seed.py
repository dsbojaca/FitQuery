import requests
import psycopg2
from dotenv import load_dotenv
import os

#cargar variables desde .env
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", 5432)
API_KEY= os.getenv("API_KEY")

#URL de la api
API_URL = "https://api.api-ninjas.com/v1/exercises"

#Lista de musculos 
MUSCULOS = ["chest", "back", "biceps", "triceps", "legs", "shoulders", "abdominals"]


#Funcion para obtener los iejercicios de la api
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

#Funcion para ingresar los datos al db
def insert_exercises(exercises):
    conn = psycopg2.connect(
        dbname= DB_NAME,
        user= DB_USER,
        password= DB_PASS,
        host= DB_HOST,
        port=DB_PORT
    )
    cur = conn.cursor()


    for ex in exercises:
        nombre = ex.get("name", "Desconocido")
        grupo = ex.get("muscle", "Otro")
        equipo = ex.get("equipment", "Sin equipo")
        dificultad = ex.get("difficulty", "Media")
        instrucciones = ex.get("instructions", "")

        cur.execute("""
            INSERT INTO fit_schema.ejercicios (nombre, grupo_muscular, equipo, dificultad, instrucciones)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT DO NOTHING
                    """, (nombre, grupo, equipo, dificultad, instrucciones))

        
    conn.commit()
    cur.close()
    conn.close()
    print(f"✅ {len(exercises)} ejercicios insertados con éxito.")



# Programa principal
if __name__ == "__main__":
    print("📡 Obteniendo ejercicios desde MuscleWiki...")
    try:
        ejercicios = fetch_exercises()
        insert_exercises(ejercicios)
    except Exception as e:
        print("❌ Error durante el scraping o inserción:", e)