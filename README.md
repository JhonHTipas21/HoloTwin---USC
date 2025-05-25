# HOLOTWIN — Sistema Inteligente de Monitoreo Energético 🎮⚡

Este repositorio contiene el módulo **frontend del sistema HOLOTWIN**, desarrollado como parte de un gemelo digital académico para la Universidad Santiago de Cali.

> **Rama activa:** `develop---Vidal`  
> **Autor del avance:** [Juan David Vidal]

---

## 🎯 Objetivo del Proyecto

Desarrollar una interfaz 3D funcional y conectada a inteligencia artificial, que permita visualizar y optimizar el consumo energético de una sala de juegos universitaria a través de un gemelo digital.

---

## 🧱 Estructura del Repositorio
```text
HoloTwin---USC/
├── frontend/
│   └── unity/
│       └── Assets/
│           └── HOLOTWIN_UI/
│               ├── Scripts/
│               │   └── UiManager.cs
│               └── README.md
├── .gitignore
└── README.md
```


---

## 💻 Frontend Unity

- Interfaz UI funcional en Unity con TextMeshPro y botones.
- Se conecta con un backend en FastAPI para:
  - Obtener recomendaciones energéticas inteligentes.
  - Exportar recomendaciones en formato PDF.

📍 Revisa: [`frontend/unity/Assets/HOLOTWIN_UI/README.md`](./frontend/unity/Assets/HOLOTWIN_UI/README.md)

---

## 🚀 Tecnologías usadas

- **Unity** 6.1.0
- **TextMeshPro** para visualización UI
- **C#** para lógica de frontend
- **FastAPI** (esperado en backend)
- **JSON + REST API**

---

## 🧪 Cómo ejecutar

1. Abre Unity y carga el proyecto desde `frontend/unity/`
2. Asegúrate de tener el backend activo en `http://localhost:8000`
3. Ejecuta la escena principal con el Canvas y prueba las funcionalidades

---

## 🧠 Estado actual del repositorio

✅ Backend removido  
✅ Estructura limpia  
✅ Frontend funcional  
✅ Conexión activa a API REST

---
