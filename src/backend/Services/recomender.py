from typing import Dict, List

def generar_recomendaciones(datos: Dict) -> List[str]:
    """
    Genera recomendaciones basadas en los datos de consumo y ambiente.
    
    Args:
        datos (Dict): Diccionario con datos de consumo y ambiente
            - consumo_total (float): Consumo total de energía
            - temperatura (float): Temperatura actual
            - ac_encendido (bool): Estado del aire acondicionado
            - hora (str): Hora actual en formato "HH:MM"
    
    Returns:
        List[str]: Lista de recomendaciones
    """
    recomendaciones = []
    
    # Analizar consumo
    if datos["consumo_total"] < 100:
        recomendaciones.append("Consumo óptimo detectado. No se requieren acciones.")
    else:
        if datos["ac_encendido"] and datos["temperatura"] < 24:
            recomendaciones.append("Considere aumentar la temperatura del aire acondicionado.")
        if "hora" in datos and (datos["hora"].startswith("11:") or datos["hora"].startswith("12:")):
            recomendaciones.append("Considere reducir el consumo durante las horas pico.")
    
    return recomendaciones if recomendaciones else ["No hay recomendaciones específicas en este momento muchas gracias."]