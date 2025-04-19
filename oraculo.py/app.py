from flask import Flask, render_template
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Configuración de la API de OpenRouter
API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.getenv("OPENROUTER_API_KEY")  # Asegúrate de que la clave esté en el archivo .env

app = Flask(__name__)
@app.route('/')
def home():
    return "¡Hola, mundo! Esta es mi primera página web con Flask."

    app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def analizar_sueño(descripcion_sueño):
    """
    Envía la descripción del sueño a la API de OpenRouter para su análisis.
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",  # Puedes cambiar el modelo si lo prefieres
        "messages": [
            {"role": "system", "content": "Eres un oráculo moderno que interpreta sueños."},
            {"role": "user", "content": f"Interpreta este sueño: {descripcion_sueño}"}
        ]
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        response.raise_for_status()  # Lanza una excepción si hay un error HTTP
        return response.json()  # Devuelve la respuesta de la API en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de OpenRouter: {e}")
        return None

@app.route("/", methodd)
def main():
    print("Bienvenido al Oráculo Moderno. Describe tu sueño y te ayudaré a interpretarlo.")
    
    # Solicitar la descripción del sueño al usuario
    descripcion_sueño = input("Por favor, describe tu sueño con el mayor detalle posible:\n")
    
    # Enviar la descripción a la API de OpenRouter
    resultado = analizar_sueño(descripcion_sueño)
    
    # Mostrar la interpretación
    if resultado:
        print("\nInterpretación del sueño:")
        print(resultado["choices"][0]["message"]["content"])  # Extraer la respuesta del modelo
    else:
        print("No se pudo obtener una interpretación en este momento.")

if __name__ == "__main__":
    main()

    from flask import Flask, render_template

