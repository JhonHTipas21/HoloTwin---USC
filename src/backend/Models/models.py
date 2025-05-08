from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..Utils.conexion_db import Base

class Usuario(Base):
    """
    Modelo que representa a un usuario en el sistema.

    Attributes:
        id (int): Identificador único del usuario
        nombre (str): Nombre de usuario, debe ser único
        contraseña (str): Contraseña hasheada del usuario
        consumos (relationship): Relación con los registros de consumo del usuario
    """
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True)
    contraseña = Column(String)
    consumos = relationship("Consumo", back_populates="usuario")

class Consumo(Base):
    """
    Modelo que representa un registro de consumo energético.

    Attributes:
        id (int): Identificador único del registro de consumo
        energia_kwh (float): Cantidad de energía consumida en kilovatios-hora
        timestamp (datetime): Fecha y hora del registro, por defecto UTC actual
        usuario_id (int): ID del usuario que registró el consumo
        usuario (relationship): Relación con el usuario que registró el consumo
    """
    __tablename__ = "consumos"
    id = Column(Integer, primary_key=True, index=True)
    energia_kwh = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"))
    usuario = relationship("Usuario", back_populates="consumos")
    