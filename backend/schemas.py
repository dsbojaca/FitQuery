from pydantic import BaseModel

class EjercicioSchema(BaseModel):
    id: int
    nombre: str
    grupo_muscular: str 
    equipo: str
    dificultad: str
    instrucciones: str  # solo si este campo existe en tu tabla

    class Config:
        orm_mode = True