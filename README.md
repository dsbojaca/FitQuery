# 🏋️‍♂️ FitQuery

⚠️ ACTUALMENTE EL DESPLIEGUE DE LA BASE DE DATOS SE ENCUENTRA CONGELADO POR LO QUE LA APLICACION NO ESTA EN UN CORRECTO FUNCIONAMINETO

FitQuery es una aplicación web que permite **buscar y filtrar ejercicios físicos** por nombre, grupo muscular y nivel de dificultad.  
El backend está desarrollado con **FastAPI**, la base de datos en **PostgreSQL** y el frontend es ligero, construido en HTML, CSS y JavaScript, con despliegue en **GitHub Pages**.


## 📲 Despliegue

### Backend: https://fitquery-sn0r.onrender.com

### Frontend: https://dsbojaca.github.io/FitQuery/

---

## 🎯 Objetivo del proyecto

El objetivo de **FitQuery** es ofrecer una herramienta sencilla, rápida y accesible para consultar ejercicios, ideal para entrenadores, deportistas y personas que desean planificar sus rutinas de forma personalizada.

---

## 📌 Funcionalidades principales

- **Búsqueda de ejercicios** por:
  - Nombre
  - Grupo muscular
  - Nivel de dificultad
- **Visualización de instrucciones** para realizar cada ejercicio.
- **Interfaz responsiva**, adaptable a móviles y escritorio.
- **Base de datos precargada** con información obtenida de la API pública de **Ninja APIs**.
- **Backend REST API** para obtener datos en formato JSON.

---

## 🛠️ Tecnologías utilizadas

### **Backend**
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)
- [Render](https://render.com/) para despliegue

### **Frontend**
- HTML5
- CSS3
- JavaScript Vanilla
- [GitHub Pages](https://pages.github.com/) para despliegue

---

## 📂 Estructura del proyecto

```plaintext
FitQuery/
│
├── backend/
│   ├── database.py
│   ├── models.py
│   ├── routes/
│   │   └── fitquery_routes.py
│   ├── schemas.py
│   ├── load.py   # Script para cargar datos desde Ninja APIs
│   └── main.py
│
├── docs/         # Frontend
│   ├── index.html
│   ├── styles.css
│   └── script.js
│
└── README.md
```

## 🚀 Instalación y ejecución local
### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/dsbojaca/FitQuery.git

cd FitQuery
```

### 2️⃣ Crear entorno virtual e instalar dependencias
```bash
python -m venv venv

source venv/bin/activate  # En Linux/Mac
venv\Scripts\activate     # En Windows

pip install -r requirements.txt
```

### 3️⃣ Configurar variables de entorno

⚠️ todos estos valores  para el DATABASE_URL seran obtenidos mas adelate cuando se cree el web server en render (para pruebas locales se puede usar un posqresql en tu maquina)

Crea un archivo **.env** en la raíz del backend con:
```bash
DATABASE_URL=postgresql+psycopg2://usuario:contraseña@localhost:5432/fitquery

NINJA_API_KEY=tu_api_key
```

### 4️⃣ Cargar datos iniciales desde Ninja APIs
```bash
python backend/load.py
```

### 5️⃣ Iniciar servidor
```bash
uvicorn backend.main:app --reload
```

## 🌐 Endpoints principales

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET    | `/ejercicios` | Lista todos los ejercicios o filtra por parámetros. |
| GET    | `/ejercicios?nombre=press` | Filtra por nombre. |
| GET    | `/ejercicios?grupo_muscular=pecho` | Filtra por grupo muscular. |
| GET    | `/ejercicios?dificultad=intermedio` | Filtra por dificultad. |



# 📌 Notas importantes

    La base de datos inicial se cargó mediante un script (load.py) que consume datos de la API de Ninja APIs, formatea la información y la almacena en PostgreSQL.

    Se configuró CORS en el backend para permitir peticiones desde GitHub Pages.

    El frontend es estático y se comunica directamente con la API del backend usando fetch().

# 🔮 Futuras mejoras

En las próximas versiones del proyecto se planea:

- Mejorar la **interfaz visual** para hacerla más atractiva y completamente responsive.
- Implementar la opción de **guardar ejercicios favoritos**.
- Permitir al usuario **crear rutinas de entrenamiento personalizadas**.
- Ampliar y optimizar la **base de datos** con más ejercicios y detalles.
- Mejorar la calidad y precisión de la información de cada ejercicio.


