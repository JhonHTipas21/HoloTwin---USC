# 🧠 HoloTwin — USC

**HoloTwin** es un gemelo digital en desarrollo del **Bloque 5** de la Universidad Santiago de Cali, enfocado en la simulación y visualización del consumo energético en tiempo real. El proyecto se construye como una aplicación de escritorio con un enfoque modular basado en una arquitectura en **tres capas**.

---

## 🚧 Estado actual del proyecto

Actualmente nos encontramos trabajando en el **frontend de escritorio con WPF (.NET 6)** para la visualización de datos, integrando gráficos mediante **LiveCharts**.

---

## 🔧 Tecnologías previstas

| Capa            | Tecnología                     |
|------------------|--------------------------------|
| **Frontend**     | WPF (.NET 6), Unity WebGL      |
| **Lógica**       | Python (Flask o FastAPI), JWT  |
| **Base de datos**| PostgreSQL                     |
| **DevOps**       | Docker, Swagger, HTTPS, Redis (opcional) |

> 🔄 El sistema seguirá una arquitectura cliente-servidor, y Unity será usado para el entorno 3D WebGL simulado. Esta primera versión se enfoca en la parte local de escritorio.

---

## ✅ Avances realizados

- Configuración del entorno en **Visual Studio Code** con `.NET 6`.
- Creación de `MainWindow.xaml` y su lógica en C# (`MainWindow.xaml.cs`).
- Implementación de dos **gráficos de líneas** usando `LiveChartsCore.SkiaSharpView.WPF`.
- Se preparó el archivo `.csproj` con los paquetes necesarios (`LiveCharts`, `SkiaSharp`, etc.).

---

## 🗂️ Estructura actual del proyecto

```plaintext
HoloTwin---USC/
├── .gitignore
├── README.md
├── docs/
│   └── (documentación futura)
├── src/
│   ├── backend/                  ← (en desarrollo por Jhon Harvey Tipas)
│   └── frontend/
│       ├── App.xaml
│       ├── App.xaml.cs
│       ├── MainWindow.xaml
│       ├── MainWindow.xaml.cs
│       ├── frontend.csproj
│       ├── bin/
│       └── obj/

---

## ▶️  Cómo ejecutar (WPF)
1. Abre una terminal y ubícate en la carpeta del frontend:
cd src/frontend

2.Restaura y ejecuta el proyecto:
dotnet restore
dotnet run

---

##📌 Requisitos
.NET 6 SDK
Visual Studio Code
Extensiones recomendadas:
C#
.NET Install Tool
NuGet Package Manager

---

##🛠️ Proyecto en desarrollo por estudiantes de la Universidad Santiago de Cali.
