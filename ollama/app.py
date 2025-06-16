import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "gemma3:1b",
    "prompt": "Hola",
    "stream": False
}

response = requests.post(url, json=data)

# Convertir el texto de la respuesta a un diccionario
respuesta_json = json.loads(response.text)

# Imprimir el valor de la clave "response"
print(respuesta_json["response"])
