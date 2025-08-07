import psycopg2
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

# Conexión a PostgreSQL
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", 5432)
)

cur = conn.cursor()

# Crear tabla si no existe
cur.execute("""
CREATE TABLE IF NOT EXISTS ejercicios (
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
