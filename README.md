
# 🚀 Backend - HoloTwin USC

## 📌 Descripción General
Sistema backend desarrollado para **HoloTwin**, implementando una arquitectura modular con **FastAPI** para:
- Gestión inteligente del consumo energético  
- Generación de recomendaciones basadas en datos  
- Integración segura con frontend y bases de datos  

---

## 🏗 Arquitectura del Sistema

### 📂 Estructura del Proyecto
```plaintext
/backend/
├── Controllers/     # Lógica de negocio
├── Models/          # Modelos de datos (SQLAlchemy)
├── Services/        # Servicios principales
├── Utils/           # Helpers y configuraciones
└── routes/          # Endpoints API
```

### 🔧 Componentes Clave
| Módulo               | Tecnologías                          | Función Principal                     |
|----------------------|--------------------------------------|---------------------------------------|
| **Autenticación**    | JWT, bcrypt                          | Gestión segura de usuarios            |
| **Base de Datos**    | PostgreSQL, SQLAlchemy               | Almacenamiento estructurado           |
| **Consumo Energético**| FastAPI, Pydantic                   | Registro y análisis de datos          |
| **Recomendaciones**  | Algoritmos personalizados            | Generación de insights inteligentes   |

---

## 🌐 API REST - Endpoints Principales

### 🔐 Autenticación
```http
POST /auth/login
```
- Valida credenciales  
- Retorna token JWT (expira en 2h)  
- Códigos de estado: `200 OK`, `401 Unauthorized`

### ⚡ Consumo Energético
```http
POST /consumo
```
- Registra nuevas mediciones  
- Parámetros: `device_id`, `kwh`, `timestamp`  
- Códigos: `201 Created`, `400 Bad Request`

### 💡 Recomendaciones
```http
GET /api/recomendaciones
```
- Variables consideradas:  
  - Consumo (kWh)  
  - Temperatura ambiente  
  - Estado de dispositivos  
  - Hora del día  

---

## 🛠 Stack Tecnológico
```mermaid
pie
    title Tecnologías Clave
    "FastAPI" : 35
    "PostgreSQL" : 25
    "SQLAlchemy" : 20
    "JWT" : 15
    "Pydantic" : 5
```

---

## 🔒 Seguridad
| Capa               | Implementación                      |
|--------------------|------------------------------------|
| **Autenticación**  | Tokens JWT + bcrypt                |
| **CORS**           | Orígenes permitidos configurados   |
| **Validación**     | Pydantic models                    |

---

## 🚀 Despliegue
### 📋 Requisitos
- Python 3.11+
- PostgreSQL 14+
- Librerías: `requirements.txt`

### ⚙️ Configuración
1. Crear archivo `.env` con variables:
   ```ini
   DB_URL=postgresql://user:pass@localhost:5432/holotwin
   JWT_SECRET=your_super_secret_key
   ```
2. Ejecutar:
   ```bash
   uvicorn main:app --reload --port 8000
   ```

---

## 🔮 Roadmap
### 🛡️ Seguridad
- [ ] Refresh tokens  
- [ ] Rate limiting  
- [ ] Logging avanzado  

### 🎛️ Funcionalidad
- [ ] Dashboard de análisis  
- [ ] Integración con sensores IoT  
- [ ] Microservicios escalables  

---

## 📚 Consideraciones Técnicas
✔️ **Escalabilidad**: Diseñado para crecimiento modular  
✔️ **Mantenibilidad**: Código documentado y testeado  
✔️ **Rendimiento**: Optimizado con conexiones en pool  

[![Deploy Example](https://img.shields.io/badge/Deploy-Render-blue)](https://render.com)
```

### Características destacadas:
1. **Jerarquía visual clara** con secciones delimitadas
2. **Tablas comparativas** para información técnica
3. **Diagrama de tecnologías** (en formato markdown)
4. **Sintaxis de código** para endpoints y estructura
5. **Badges** para integración con servicios
6. **Emojis** para mejor scaneo visual (opcional)
7. **Listas de roadmap** con checkboxes

