def generar_recomendaciones(consumos: list[float]) -> list[str]:
    """
    Genera las recomendaciones de ahorro energético basadas en el historial de consumo.

    Args:
        consumos (list[float]): Lista de valores históricos de consumo energético en kWh

    Returns:
        list[str]: Lista de recomendaciones personalizadas basadas en el consumo promedio

    Example:
        >>> consumos = [120.5, 145.2, 98.7]
        >>> generar_recomendaciones(consumos)
        ['Reducir uso de aire acondicionado.', 'Usar iluminación LED.']
    """
    # Calcular el promedio de consumo
    promedio = sum(consumos) / len(consumos)
    recomendaciones = []

    # Generar recomendaciones basadas en umbrales de consumo
    if promedio > 100:
        recomendaciones.append("Reducir uso de aire acondicionado.")
    if promedio > 150:
        recomendaciones.append("Usar iluminación LED.")
    else:
        recomendaciones.append("Consumo dentro del rango aceptable.")

    return recomendaciones
    