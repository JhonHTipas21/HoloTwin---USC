from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from ..Services.recomender import generar_recomendaciones

router = APIRouter()

class SensorInput(BaseModel):
    consumo_total: float
    temperatura: float
    ac_encendido: bool
    hora: str

class RecomendacionResponse(BaseModel):
    recomendaciones: List[str]

# Endpoint POST original para la recomendaciones
@router.post("/recomendaciones", response_model=RecomendacionResponse)
def crear_recomendaciones(data: SensorInput):
    try:
        recomendaciones = generar_recomendaciones(data.dict())
        return {"recomendaciones": recomendaciones}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Nuevo endpoint GET para pruebas
@router.get("/recomendaciones", response_model=RecomendacionResponse)
def obtener_recomendaciones():
    datos_prueba = {
        "consumo_total": 80,
        "temperatura": 22,
        "ac_encendido": False,
        "hora": "10:30"
    }
    try:
        recomendaciones = generar_recomendaciones(datos_prueba)
        return {"recomendaciones": recomendaciones}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))