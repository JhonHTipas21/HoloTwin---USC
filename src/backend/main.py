from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .Controllers import auth_controller, consumo_controller, recomendaciones_controller

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_controller.router)
app.include_router(consumo_controller.router)
app.include_router(recomendaciones_controller.router)