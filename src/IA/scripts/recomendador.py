def generar_recomendaciones(consumos: list[float]):
    promedio = sum(consumos) / len(consumos)
    recomendaciones = []

    if promedio > 100:
        recomendaciones.append("Reducir uso de aire acondicionado.")
    if promedio > 150:
        recomendaciones.append("Usar iluminación LED.")
    else:
        recomendaciones.append("Consumo dentro del rango aceptable.")

    return recomendaciones
