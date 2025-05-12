from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

"""
Módulo de configuración y conexión a la base de datos PostgreSQL.
Este módulo establece la conexión con la base de datos y proporciona
las herramientas necesarias para la interacción con la misma.
"""

# Configuración de la conexión a la base de datos
DATABASE_URL = "postgresql://postgres:jhon2003@localhost:5432/holotwindb"
"""
URL de conexión a la base de datos con el formato:
postgresql://usuario:contraseña@host:puerto/nombre_base_datos
"""

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL)
"""
Motor de SQLAlchemy que gestiona la conexión con la base de datos.
Este objeto maneja el pool de conexiones y la comunicación con PostgreSQL.
"""

# Configurar la sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
"""
Fábrica de sesiones que creará instancias de sesión para interactuar con la base de datos.
autocommit=False: Los cambios deben confirmarse explícitamente
autoflush=False: Los cambios no se envían automáticamente a la base de datos
"""

# Clase base para los modelos
Base = declarative_base()
"""
Clase base declarativa de SQLAlchemy.
Todas las clases de modelo deben heredar de esta clase para
mapear las tablas de la base de datos en Postgres.
"""