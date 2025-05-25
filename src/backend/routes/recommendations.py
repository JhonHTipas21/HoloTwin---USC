# src/backend/routes/recommendations.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List
import os

from src.backend.Services.recomender import generar_recomendacion_energia
from src.backend.Services.pdf_generator import exportar_reporte_pdf

router = APIRouter(prefix="/api/recomendaciones", tags=["IA Recomendaciones"])

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

@router.post("/recomendar/pdf")
def recomendar_y_exportar_pdf(data: RecomendacionRequest):
    try:
        recomendacion = generar_recomendacion_energia(data.sala, data.consumo, data.dispositivos)

        # ✅ Crear carpeta si no existe
        carpeta_reportes = os.path.join(os.getcwd(), "reportes")
        os.makedirs(carpeta_reportes, exist_ok=True)

        # ✅ Generar PDF
        file_path = exportar_reporte_pdf(
            nombre_usuario="admin",
            consumo=data.consumo,
            dispositivos=data.dispositivos,
            recomendacion=recomendacion,
            sala=data.sala
        )

        # ✅ Mover PDF generado a carpeta /reportes
        nuevo_path = os.path.join(carpeta_reportes, os.path.basename(file_path))
        os.replace(file_path, nuevo_path)

        return {
            "msg": "Reporte generado exitosamente",
            "recomendacion": recomendacion,
            "ruta_pdf": f"/api/recomendaciones/reporte/{os.path.basename(nuevo_path)}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/reporte/{nombre_archivo}")
def descargar_pdf(nombre_archivo: str):
    carpeta_reportes = os.path.join(os.getcwd(), "reportes")
    ruta_archivo = os.path.join(carpeta_reportes, nombre_archivo)

    if not os.path.exists(ruta_archivo):
        raise HTTPException(status_code=404, detail="Archivo no encontrado")

    return FileResponse(ruta_archivo, media_type='application/pdf', filename=nombre_archivo)
