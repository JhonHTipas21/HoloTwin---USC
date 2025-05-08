from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..Models import models
from ..Utils.conexion_db import SessionLocal
from datetime import datetime

# Crear una instancia del router FastAPI para los endpoints de consumo
router = APIRouter()

def get_db():
    """
    Función de dependencia de base de datos que crea y gestiona sesiones.
    Yields:
        Session: Sesión de base de datos SQLAlchemy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/consumo")
def registrar_consumo(energia_kwh: float, usuario_id: int, db: Session = Depends(get_db)):
    """
    Registra un nuevo consumo de energía para un usuario específico.

    Args:
        energia_kwh (float): Cantidad de energía consumida en kilovatios-hora
        usuario_id (int): Identificador del usuario que registra el consumo
        db (Session): Dependencia de sesión de base de datos

    Returns:
        dict: Mensaje de confirmación del registro

    Example:
        {
            "msg": "Consumo registrado"
        }
    """
    # Crear nueva instancia de consumo
    nuevo = models.Consumo(energia_kwh=energia_kwh, usuario_id=usuario_id)
    
    # Agregar y guardar en la base de datos
    db.add(nuevo)
    db.commit()
    
    return {"msg": "Consumo registrado"}

    