from fastapi import APIRouter, Depends, HTTPException
from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ..Utils.conexion_db import SessionLocal
from ..Models import models

router = APIRouter()
SECRET_KEY = "CLAVESECRETA"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/auth/login")
def login(nombre: str, contraseña: str, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(models.Usuario.nombre == nombre).first()
    if not usuario or not pwd_context.verify(contraseña, usuario.contraseña):
        raise HTTPException(status_code=400, detail="Credenciales inválidas")

    token = jwt.encode({"sub": usuario.nombre, "exp": datetime.utcnow() + timedelta(hours=2)}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}
