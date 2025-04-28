# src/backend/Utils/conexion_db.py
# codigo encargado de establecer la conexión a la base de datos MySQL
import mysql.connector

def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="HoloTwinDB"
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
        return None
