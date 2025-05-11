# HoloTwin - USC

## Descripción General
**HOLOTWIN** es un gemelo digital diseñado para la monitorización, análisis y simulación del consumo energético en la sala de juegos del Bloque 5 de la Universidad Santiago de Cali. 

El proyecto combina:
- Visualización 3D interactiva
- Generación y análisis de datos mediante IA
- Gestión avanzada de información

Su objetivo principal es promover la sostenibilidad energética en entornos universitarios mediante tecnologías innovadoras.

## Arquitectura del Sistema

### 🖥 Frontend - Visualización 3D
**Tecnología principal:** Unity (Motor gráfico 3D)  
**Lenguaje de programación:** C#  

**Funcionalidades:**
- Visualización en tiempo real del consumo energético
- Simulaciones de eficiencia energética
- Visualización de alertas y recomendaciones generadas por IA

### ⚙ Backend - Lógica y Comunicación
**Framework principal:** FastAPI (Python)  

**Stack tecnológico:**
- Python 3.10+
- FastAPI
- SQLAlchemy
- Pydantic
- JWT (JSON Web Tokens)
- Uvicorn

**Características:**
- Arquitectura API RESTful modular
- Servidor ASGI (Uvicorn) para alto rendimiento en operaciones asíncronas

### 🗃 Base de Datos
**Motor de base de datos:** PostgreSQL  
**ORM:** SQLAlchemy  

**Estructura principal:**
| Tabla              | Descripción                                  |
|--------------------|---------------------------------------------|
| `users`            | Credenciales, roles y tokens de acceso      |
| `devices`          | Equipos eléctricos y sus metadatos          |
| `energy_data`      | Registros de consumo por dispositivo        |
| `recommendations`  | Salidas del sistema de IA y recomendaciones |

## Contribuciones
¡Las contribuciones son bienvenidas! Por favor, abre un issue o pull request para discutir mejoras al proyecto.


