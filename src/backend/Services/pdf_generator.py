# src/backend/Utils/pdf_generator.py

import os
from fpdf import FPDF
from datetime import datetime

def exportar_reporte_pdf(nombre_usuario: str, consumo: float, dispositivos: list, recomendacion: str, sala: str = "Bloque 5") -> str:
    # 📁 Definir la ruta absoluta a la carpeta 'reportes'
    carpeta_reportes = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'reportes'))

    # 📁 Crear la carpeta si no existe
    os.makedirs(carpeta_reportes, exist_ok=True)

    # 📝 Inicializar el PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # 🧾 Título y cabecera
    pdf.cell(200, 10, txt=f"Reporte Energético - {sala}", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Usuario: {nombre_usuario}", ln=True)
    pdf.cell(200, 10, txt=f"Consumo: {consumo} kWh/día", ln=True)
    pdf.cell(200, 10, txt=f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)

    # 🔌 Lista de dispositivos
    pdf.ln(10)
    pdf.cell(200, 10, txt="Dispositivos activos:", ln=True)
    for d in dispositivos:
        pdf.cell(200, 10, txt=f"- {d}", ln=True)

    # 💡 Recomendaciones
    pdf.ln(10)
    pdf.multi_cell(200, 10, txt=f"Recomendaciones de IA:\n{recomendacion}")

    # 💾 Ruta final del archivo PDF
    file_name = f"reporte_consumo_{nombre_usuario}.pdf"
    file_path = os.path.join(carpeta_reportes, file_name)

    # 💽 Guardar PDF
    pdf.output(file_path)

    return file_path
