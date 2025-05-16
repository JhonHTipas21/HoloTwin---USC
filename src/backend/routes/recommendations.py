from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from src.backend.Services.recomender import generar_recomendacion_energia

router = APIRouter()

class RecomendacionRequest(BaseModel):
    sala: str
    consumo: float
    dispositivos: List[str]

@router.post("/recomendar")
def recomendar_energia(data: RecomendacionRequest):
    try:
        recomendacion = generar_recomendacion_energia(data.sala, data.consumo, data.dispositivos)
        return {"recomendacion": recomendacion}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))