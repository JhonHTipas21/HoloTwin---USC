# src/backend/Models/models.py

from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..Utils.base import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True)
    contraseña = Column(String)
    consumos = relationship("Consumo", back_populates="usuario")

class Consumo(Base):
    __tablename__ = "consumos"
    id = Column(Integer, primary_key=True, index=True)
    energia_kwh = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="consumos")
