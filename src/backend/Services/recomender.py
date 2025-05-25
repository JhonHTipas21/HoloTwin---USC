from .gemini_client import generate_recommendation


def generar_recomendacion_energia(sala: str, consumo: float, dispositivos: list) -> str:
    """
    Genera una recomendación de optimización energética basada en los datos de entrada del gemelo digital.
    """
    prompt = (
        f"Estás actuando como un asesor inteligente de eficiencia energética. Estoy desarrollando un gemelo digital "
        f"para el salón académico '{sala}' de la Universidad Santiago de Cali. El consumo energético promedio es de "
        f"{consumo} kWh por día. Los dispositivos presentes en el salón son: {', '.join(dispositivos)}.\n\n"
        "Tu objetivo es analizar este escenario y generar recomendaciones detalladas para reducir el consumo de energía "
        "sin comprometer la experiencia o el confort de los usuarios. Incluye sugerencias sobre:\n"
        "- Comportamientos sostenibles.\n"
        "- Automatización y sensores inteligentes.\n"
        "- Optimización de uso de equipos.\n"
        "- Posibles fuentes de energía renovable o estrategias de desconexión inteligente.\n\n"
        "Redacta tu respuesta como un informe breve pero claro para que pueda ser usado en un reporte técnico."
    )

    respuesta = generate_recommendation(prompt)
    return respuesta
