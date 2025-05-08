from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..Utils.conexion_db import SessionLocal
from ..Models import models
from ..IA_scripts import recomendador

router = APIRouter()

@router.get("/recomendaciones")
def obtener_recomendaciones(usuario_id: int, db: Session = Depends(SessionLocal)):
    consumos = db.query(models.Consumo).filter(models.Consumo.usuario_id == usuario_id).all()
    valores = [c.energia_kwh for c in consumos]
    return {"recomendaciones": recomendador.generar_recomendaciones(valores)}
