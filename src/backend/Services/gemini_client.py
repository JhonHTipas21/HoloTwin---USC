import os
import requests
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")
GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", 0.7))


def generate_recommendation(prompt: str) -> str:
    """
    Envía un prompt a la API de Gemini y retorna la respuesta generada.
    """
    headers = {
        "Content-Type": "application/json"
    }

    params = {
        "key": GEMINI_API_KEY
    }

    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": GEMINI_TEMPERATURE,
            "topK": 1,
            "topP": 1
        }
    }

    response = requests.post(GEMINI_API_URL, headers=headers, params=params, json=data)

    if response.status_code == 200:
        try:
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "No se pudo interpretar la respuesta de Gemini."
    else:
        return f"Error en la solicitud a Gemini: {response.status_code} - {response.text}"
