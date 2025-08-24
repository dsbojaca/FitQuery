from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from backend.database import Base





class Ejercicio(Base):
    __tablename__ = 'ejercicios'
    __table_args__ = {'schema': 'fit_schema'}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    grupo_muscular = Column(String)
    equipo = Column(String)
    dificultad = Column(String)
    instrucciones = Column(Text)

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'schema': 'fit_schema'}

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)