from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .Controllers import auth_controller, consumo_controller, recomendaciones_controller

"""
Archivo principal de la aplicación FastAPI.
Configura la aplicación, el middleware CORS y registra los routers de los controladores.
"""

# Crear la instancia principal de la aplicación FastAPI
app = FastAPI()

# Configurar el middleware CORS para permitir peticiones desde otros dominios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # Permite peticiones desde cualquier origen
    allow_credentials=True,   # Permite enviar credenciales (cookies, headers de autenticación)
    allow_methods=["*"],     # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],     # Permite todos los headers HTTP
)

# Registrar los routers de los diferentes controladores
app.include_router(auth_controller.router)          # Router para autenticación
app.include_router(consumo_controller.router)       # Router para gestión de consumos
app.include_router(recomendaciones_controller.router)  # Router para recomendaciones