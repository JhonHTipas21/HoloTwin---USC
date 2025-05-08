from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..Utils.conexion_db import SessionLocal
from ..Models import models

# Crear una instancia del router FastAPI para los endpoints de autenticación
router = APIRouter()

# Configuración de constantes de seguridad
SECRET_KEY = "CLAVESECRETA"  # Clave utilizada para la encriptación del token JWT
ALGORITHM = "HS256"  # Algoritmo utilizado para la generación del token JWT
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")  # Configuración del hash de contraseñas

def get_db():
    """
    Función de dependencia de base de datos que crea y gestiona sesiones.
    Yields:
        Session: Sesión de base de datos SQLAlchemy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/login")
def login(nombre: str, contraseña: str, db: Session = Depends(get_db)):
    """
    Autenticar usuario y generar token JWT.

    Args:
        nombre (str): Nombre de usuario para autenticación
        contraseña (str): Contraseña del usuario
        db (Session): Dependencia de sesión de base de datos

    Returns:
        dict: Contiene el token de acceso JWT si la autenticación es exitosa

    Raises:
        HTTPException: Error 400 si las credenciales son inválidas
    """
    # Consultar usuario en la base de datos
    usuario = db.query(models.Usuario).filter(models.Usuario.nombre == nombre).first()
    
    # Verificar si el usuario existe y la contraseña es correcta
    if not usuario or not pwd_context.verify(contraseña, usuario.contraseña):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    # Generar token JWT con expiración de 2 horas
    token = jwt.encode(
        {
            "sub": usuario.nombre,
            "exp": datetime.utcnow() + timedelta(hours=2)
        },
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return {"access_token": token}
    