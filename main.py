
import os
import google.generativeai as genai

# Configuración de la API de Gemini
# Requiere que la variable de entorno GEMINI_API_KEY esté configurada
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("No se encontró la API Key. Configure la variable GEMINI_API_KEY.")

genai.configure(api_key=api_key)

def calcular_vpn(flujos_efectivo, tasa_descuento):
    """
    Calcula el Valor Presente Neto (VPN) de una serie de flujos de efectivo.
    """
    vpn = sum([f / (1 + tasa_descuento)**i for i, f in enumerate(flujos_efectivo)])
    return vpn

def analizar_viabilidad_con_gemini(vpn, inversion, flujo_anual, n_anios, tasa):
    """
    Envía los resultados financieros a Gemini para obtener un dictamen automatizado.
    """
    modelo = genai.GenerativeModel('gemini-2.0-flash')
    prompt = (
        f"Actúa como un analista experto en Ingeniería Económica. "
        f"Se ha evaluado la instalación de un banco de capacitores con una inversión inicial de ${abs(inversion)} MXN "
        f"y ahorros de efectivo anuales de ${flujo_anual} MXN durante {n_anios} años. "
        f"La tasa de descuento (TMAR) es del {tasa*100}%. El Valor Presente Neto (VPN) calculado matemáticamente es ${vpn:.2f} MXN. "
        f"Redacta un dictamen ejecutivo formal (máximo 2 párrafos) indicando si el proyecto se debe aceptar o rechazar. "
        f"Justifica tu respuesta basándote estrictamente en el criterio de aceptación del VPN."
    )
    
    respuesta = modelo.generate_content(prompt)
    return respuesta.text

def main():
    # Parámetros financieros del proyecto
    tasa_descuento = 0.10 
    inversion_inicial = -15000
    flujo_anual = 4500
    n_anios = 5
    flujos_efectivo = [inversion_inicial] + [flujo_anual] * n_anios

    print("======================================================")
    print("SISTEMA DE EVALUACIÓN ECONÓMICA DE PROYECTOS (VPN/IA)")
    print("======================================================")
    print(f"Inversión Inicial: ${abs(inversion_inicial)} MXN")
    print(f"Ahorro Anual Proyectado: ${flujo_anual} MXN por {n_anios} años")
    print(f"Tasa de Descuento (TMAR): {tasa_descuento*100}%")

    # 1. Cálculo Matemático (El programa resuelve el problema)
    vpn = calcular_vpn(flujos_efectivo, tasa_descuento)
    print("\n[+] RESULTADO MATEMÁTICO:")
    print(f"Valor Presente Neto (VPN): ${vpn:.2f} MXN")

    # 2. Integración con Gemini AI (La IA propone la solución)
    print("\n[+] ANALIZANDO DATOS CON GEMINI AI...")
    try:
        dictamen = analizar_viabilidad_con_gemini(vpn, inversion_inicial, flujo_anual, n_anios, tasa_descuento)
        print("\nDICTAMEN EJECUTIVO:")
        print("------------------------------------------------------")
        print(dictamen)
        print("------------------------------------------------------")
    except Exception as e:
        print(f"\n[!] Error en la conexión con la API: {e}")

if __name__ == "__main__":
    main()