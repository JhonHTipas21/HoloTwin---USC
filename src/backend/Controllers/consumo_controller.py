from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..Models import models
from ..Utils.conexion_db import SessionLocal
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/consumo")
def registrar_consumo(energia_kwh: float, usuario_id: int, db: Session = Depends(get_db)):
    nuevo = models.Consumo(energia_kwh=energia_kwh, usuario_id=usuario_id)
    db.add(nuevo)
    db.commit()
    return {"msg": "Consumo registrado"}
