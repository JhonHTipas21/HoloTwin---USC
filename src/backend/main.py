# src/backend/main.py

import sys
import os
from dotenv import load_dotenv

# 🔥 Cargar variables del entorno desde el archivo .env
load_dotenv()

# Añadir el directorio raíz al path para facilitar imports relativos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles  # ✅ para servir archivos estáticos

# Importar controladores y rutas
from .Controllers import auth_controller, consumo_controller, recomendaciones_controller
from .routes import recommendations, gemini_routes

# Crear la instancia principal de la aplicación FastAPI
app = FastAPI(
    title="HOLOTWIN API",
    version="0.1.0",
    description="API para simulación y recomendaciones energéticas en la Universidad Santiago de Cali"
)

# Configurar middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, deberías limitar esto a dominios confiables
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Servir archivos PDF desde /reportes
app.mount("/reportes", StaticFiles(directory="reportes"), name="reportes")

# Incluir routers
app.include_router(auth_controller.router)
app.include_router(consumo_controller.router)
app.include_router(recomendaciones_controller.router)
app.include_router(recommendations.router, prefix="/api")         # Recomendaciones IA local
app.include_router(gemini_routes.router, prefix="/api/gemini")    # Recomendaciones con Gemini
