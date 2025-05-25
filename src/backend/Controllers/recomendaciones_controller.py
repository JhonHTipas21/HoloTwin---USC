# src/backend/Controllers/recomendaciones_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..Utils.conexion_db import get_db
from ..Models import models
from ..IA_scripts import recomendador

router = APIRouter()

@router.get("/recomendaciones")
def obtener_recomendaciones(usuario_id: int, db: Session = Depends(get_db)):
    """
    Obtiene recomendaciones basadas en el historial de consumo del usuario.

    Args:
        usuario_id (int): ID del usuario
        db (Session): Sesión de base de datos

    Returns:
        dict: Recomendaciones generadas por el sistema
    """
    try:
        consumos = db.query(models.Consumo).filter(models.Consumo.usuario_id == usuario_id).all()

        if not consumos:
            return {"recomendaciones": ["No se encontraron consumos para este usuario."]}

        valores = [c.energia_kwh for c in consumos]
        recomendaciones = recomendador.generar_recomendaciones(valores)

        return {"recomendaciones": recomendaciones}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
