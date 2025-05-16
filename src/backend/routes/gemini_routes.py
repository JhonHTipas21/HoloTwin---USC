# src/backend/routes/gemini_routes.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.backend.IA_scripts.ia_energy_assistant import obtener_recomendacion_gemini


router = APIRouter(prefix="/gemini", tags=["IA Recommendations"])

class ConsumoEnergiaInput(BaseModel):
    datos: str

@router.post("/recomendar")
def recomendar_consumo(data: ConsumoEnergiaInput):
    try:
        resultado = obtener_recomendacion_gemini(data.datos)
        return {"recomendacion": resultado}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
