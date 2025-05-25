# HOLOTWIN - Frontend Unity

Este módulo contiene el avance funcional del frontend del sistema HOLOTWIN, desarrollado en Unity y conectado a un backend construido con FastAPI.

---

## 🎯 ¿Qué hace este módulo?

- Permite enviar información de consumo energético y dispositivos activos a un backend REST.
- Recibe recomendaciones inteligentes generadas por IA.
- Muestra el consumo y recomendaciones en tiempo real.
- Permite exportar las recomendaciones en PDF.

---

## 🧱 Estructura
```text
HOLOTWIN_UI/
├── Scripts/
│   └── UiManager.cs
└── README.md
```

---

## 🚀 Cómo probarlo

1. Abre el proyecto Unity y carga la escena con el Canvas.
2. Asigna el script `UiManager.cs` a un GameObject vacío llamado `UIManager`.
3. Enlaza los elementos:
   - `txtConsumoActual`: componente TextMeshPro para mostrar consumo.
   - `txtRecomendacion`: componente TextMeshPro para mostrar sugerencias.
   - `btnObtenerRecomendacion`: botón que consulta a la IA.
   - `btnExportarPDF`: botón que genera PDF.

---

## 🔗 Backend esperado

- `POST /api/recomendaciones/recomendar` → Devuelve texto de recomendación.
- `POST /api/recomendaciones/recomendar/pdf` → Devuelve recomendación en PDF.

> Asegúrate de tener el backend activo en `http://localhost:8000`.

---
