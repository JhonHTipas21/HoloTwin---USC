import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .Controllers import auth_controller, consumo_controller, recomendaciones_controller
from .routes import recommendations, gemini_routes  # Nueva ruta importada

"""
Archivo principal de la aplicación FastAPI.
Configura la aplicación, el middleware CORS y registra los routers de los controladores.
"""

# Crear la instancia principal de la aplicación FastAPI
app = FastAPI()

# Configurar el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar los routers existentes
app.include_router(auth_controller.router)
app.include_router(consumo_controller.router)
app.include_router(recomendaciones_controller.router)
app.include_router(recommendations.router, prefix="/api")

# Registrar el nuevo router para recomendaciones vía Gemini
app.include_router(gemini_routes.router, prefix="/api/gemini")
