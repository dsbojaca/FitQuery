from fastapi import APIRouter, Depends
from backend.auth import get_current_user
from backend import models

router = APIRouter(
    prefix="/inicio",
    tags=["Inicio"]
)

@router.get("/")
def inicio(user: models.User = Depends(get_current_user)):
    """
    Ruta protegida: Solo accesible con un token válido.
    """
    return {
        "msg": f"Bienvenido {user.username}, ya tienes acceso a la página de inicio."
    }