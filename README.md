# HoloTwin---USC
1. Descripción General
HOLOTWIN es un gemelo digital desarrollado para la monitorización, análisis y simulación del consumo energético de la sala de juegos del Bloque 5 en la Universidad Santiago de Cali. Este proyecto integra visualización 3D (Unity), generación y análisis de datos energéticos (IA), y gestión de información (backend con FastAPl y PostgreSQL), promoviendo la sostenibilidad energética en entornos universitarios.
2. Componentes Tecnológicos
2.1 Frontend - Visualización y Simulación
• Tecnología principal: Unity (Motor gráfico 3D)
• Lenguaje: C#
• Objetivo: Visualizar en tiempo real el consumo energético, ejecutar simulaciones de eficiencia, mostrar alertas o recomendaciones del sistema de lA.
2.2 Backend - Núcleo Lógico y
Comunicacional
• Framework: FastAPI (Python)
• Lenguajes y librerías: Python 3.10+, FastAPI,
SQLAlchemy, Pydantic, JWT, Uvicorn
• Arquitectura: API RESTful modular
• Servidor ASGI: Uvicorn, por su alto rendimiento en aplicaciones asincrónicas.
2.3 Base de Datos
• Motor: PostgreSQL
• ORM: SQLAlchemy
• Estructura:
• users (credenciales, roles, tokens)
• devices (equipos eléctricos y metadatos)
• energy_data (consumo energético por dispositivo, timestamp, fuente)
• recommendations (salidas del sistema de
IA)
2.4 Sensores Sintéticos
• Generación de datos ficticios: Scripts Python que simulan valores realistas para consumo energético, humedad, temperatura, tiempo de uso por dispositivo.
2.5 Motor de Inteligencia Artificial
• Modelo supervisado (ML): Regresión múltiple, árbol de decisión, o Random Forest para predecir consumo y COz.
• Entrenamiento local: Dataset generado con sensores sintéticos.
• Output: JSON con sugerencias de optimización energética.
