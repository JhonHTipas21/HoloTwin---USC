# src/IA/predictor.py
#CODIGO ENCARGADO DE HACER PREDICCIONES DE CONSUMO ENERGÉTICO UTILIZANDO UN MODELO DE REGRESIÓN LINEAL
import numpy as np
from sklearn.linear_model import LinearRegression

# Datos de ejemplo (X: hora del día, Y: consumo energético)
X = np.array([[8], [12], [15], [18], [21]])  # Horas
y = np.array([200, 450, 400, 600, 500])      # Consumo en Watts

# Crear modelo
modelo = LinearRegression()
modelo.fit(X, y)

# Predicción de consumo a las 17h
hora = np.array([[17]])
prediccion = modelo.predict(hora)

print(f"Predicción de consumo a las 17h: {prediccion[0]:.2f} Watts")
