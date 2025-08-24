from pydantic import BaseModel, EmailStr


class EjercicioSchema(BaseModel):
    id: int
    nombre: str
    grupo_muscular: str 
    equipo: str
    dificultad: str
    instrucciones: str  # solo si este campo existe en tu tabla

    class Config:
        from_attributes = True  # ✅ en lugar de orm_mode


class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    
    class Config:
        from_attributes = True  # ✅


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str