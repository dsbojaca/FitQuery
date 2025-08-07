import psycopg2
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")


# Conexión a PostgreSQL
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)

cur = conn.cursor()

# Crear tabla si no existe
cur.execute("""
CREATE TABLE IF NOT EXISTS fit_schema.ejercicios (
    id SERIAL PRIMARY KEY,
    nombre TEXT NOT NULL,
    grupo_muscular TEXT,
    equipo TEXT,
    dificultad TEXT,
    url TEXT
);
""")

conn.commit()
cur.close()
conn.close()

print("✅ Tabla 'ejercicios' creada o ya existente.")
