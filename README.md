# Evaluación Económica con IA (Gemini)

Este es un programa de Ingeniería Económica diseñado para calcular la viabilidad de un proyecto industrial (ej. instalación de un banco de capacitores) mediante el análisis del Valor Presente Neto (VPN). 

El sistema realiza el cálculo matemático y utiliza la API de Google Gemini para redactar un dictamen ejecutivo automático sobre la rentabilidad del proyecto.

## Requisitos
- Python 3.8+
- `google-generativeai`

## Uso
1. Configurar la variable de entorno con la clave de Gemini:
   `export GEMINI_API_KEY="tu_clave"`
2. Ejecutar el script:
   `python main.py`
