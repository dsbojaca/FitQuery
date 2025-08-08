from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ejercicio(Base):
    __tablename__ = 'ejercicios'
    __table_args__ = {'schema': 'fit_schema'}

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    grupo_muscular = Column(String)
    equipo = Column(String)
    dificultad = Column(String)
    instrucciones = Column(Text)