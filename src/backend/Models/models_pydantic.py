from pydantic import BaseModel
from typing import List

class RecomendacionRequest(BaseModel):
    sala: str
    consumo: float  # en kWh/día
    dispositivos: List[str]
