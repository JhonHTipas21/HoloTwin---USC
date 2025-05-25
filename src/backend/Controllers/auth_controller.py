# src/backend/Controllers/auth_controller.py

from fastapi import APIRouter, Depends, HTTPException
from jose import JWTError, jwt
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from ..Utils.conexion_db import SessionLocal
from ..Models import models

# Configuración de seguridad
SECRET_KEY = "CLAVESECRETA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 2

# Crear instancia del router
router = APIRouter(prefix="/auth", tags=["Login"])

# Dependencia de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(nombre: str, contraseña: str, db: Session = Depends(get_db)):
    """
    Autenticar usuario y generar token JWT (con contraseñas en texto plano).
    """
    # Buscar usuario por nombre
    usuario = db.query(models.Usuario).filter(models.Usuario.nombre == nombre).first()

    # Validación de credenciales (comparación directa en texto plano)
    if not usuario or usuario.contraseña != contraseña:
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    # Crear token JWT
    token_data = {
        "sub": usuario.nombre,
        "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

    return {
        "access_token": token,
        "token_type": "bearer"
    }
