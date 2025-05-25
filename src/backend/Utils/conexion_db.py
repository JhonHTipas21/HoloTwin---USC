from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base

# Configuración de la conexión a la base de datos
DATABASE_URL = "postgresql://postgres:jhon2003@localhost:5432/holotwindb"

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)

# Configurar la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependencia para obtener una sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
