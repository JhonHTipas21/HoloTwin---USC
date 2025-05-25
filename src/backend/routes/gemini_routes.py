# src/backend/routes/gemini_routes.py

from fastapi import APIRouter, HTTPException
from src.backend.Models.models_pydantic import RecomendacionRequest
from src.backend.Services.recomender import generar_recomendacion_energia
from src.backend.Services.pdf_generator import exportar_reporte_pdf

router = APIRouter(prefix="/api", tags=["IA Recommendations"])


@router.post("/recomendar")
def recomendar_consumo(data: RecomendacionRequest):
    try:
        # Generar recomendación usando Gemini
        resultado = generar_recomendacion_energia(data.sala, data.consumo, data.dispositivos)

        # Exportar resultado a PDF
        pdf_path = exportar_reporte_pdf(
            nombre_usuario="usuario_demo",  # puedes reemplazarlo por el nombre del usuario autenticado
            consumo=data.consumo,
            dispositivos=data.dispositivos,
            recomendacion=resultado,
            sala=data.sala
        )

        # Retornar la recomendación y el path del PDF generado
        return {
            "recomendacion": resultado,
            "reporte_pdf": pdf_path
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar recomendación: {str(e)}")
