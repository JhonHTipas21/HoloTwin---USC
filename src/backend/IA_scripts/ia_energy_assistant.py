# src/backend/IA_scripts/ia_energy_assistant.py

from backend.Services.gemini_client import generate_recommendation


def obtener_recomendacion_gemini(datos_consumo: str) -> str:
    """
    Lógica para preparar y limpiar datos antes de enviarlos a Gemini.
    """
    datos_limpios = datos_consumo.strip()
    recomendacion = generate_recommendation(datos_limpios)
    return recomendacion
