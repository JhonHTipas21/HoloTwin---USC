from .gemini_client import generate_recommendation


def generar_recomendacion_energia(sala: str, consumo: float, dispositivos: list) -> str:
    """
    Genera una recomendación de optimización energética basada en los datos de entrada.
    """
    prompt = (
        f"Estoy desarrollando un gemelo digital para la sala de juegos '{sala}', que consume aproximadamente "
        f"{consumo} kWh. Entre los dispositivos hay: {', '.join(dispositivos)}. "
        "¿Podrías generar una recomendación de eficiencia energética que ayude a reducir el consumo eléctrico "
        "en este espacio, considerando también el confort de los usuarios y posibles medidas sostenibles como sensores, "
        "automatización, o energía renovable?"
    )

    respuesta = generate_recommendation(prompt)
    return respuesta
