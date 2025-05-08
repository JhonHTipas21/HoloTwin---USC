from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..Utils.conexion_db import SessionLocal
from ..Models import models
from ..IA_scripts import recomendador

# Crear una instancia del router FastAPI para los endpoints de recomendaciones
router = APIRouter()

@router.get("/recomendaciones")
def obtener_recomendaciones(usuario_id: int, db: Session = Depends(SessionLocal)):
    """
    Obtiene recomendaciones personalizadas basadas en el historial de consumo de un usuario.

    Args:
        usuario_id (int): Identificador del usuario para el cual se generarán las recomendaciones
        db (Session): Dependencia de sesión de base de datos

    Returns:
        dict: Diccionario conteniendo una lista de recomendaciones generadas
              basadas en el patrón de consumo del usuario

    Example:
        {
            "recomendaciones": [
                "Recomendación 1",
                "Recomendación 2",
                ...
            ]
        }
    """
    # Obtener todos los registros de consumo del usuario
    consumos = db.query(models.Consumo).filter(models.Consumo.usuario_id == usuario_id).all()
    
    # Extraer los valores de energía de los consumos
    valores = [c.energia_kwh for c in consumos]
    
    # Generar y retornar las recomendaciones usando el modelo de IA
    return {"recomendaciones": recomendador.generar_recomendaciones(valores)}

    