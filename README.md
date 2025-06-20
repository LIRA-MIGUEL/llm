# llm
Modelos de lenguaje largo

# Se crea el entorno virtual
python -m venv .venv

# Instala requests de python
pip install requests

# source .venv/bin/activate
accede a tu entorno virtual

# Instala ollama compatible con linux
curl -fsSL https://ollama.com/install.sh | sh
# 
ollama serve

# Ejecuta el modelo de ia gemma3
ollama run gemma3:1b 

# Ejemplo con RES API
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"Hola",
  "stream": false
}'

# Api Key
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

# Ejecutar aplicacion fast api
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Carpeta backend
Contiene el archivo main y la carpeta templates con un index. Este codigo hconvierte el lenguaje humano y lo convierte en consultas de numpy y pandas.(Pendiente a terminar)

# Carpeta ollama
contiene ejemplos con modelos de grop

# Archivo main.py y templates en la raiz del proyecto
Proyecto donde cargas un csv le haces una pregunta y te devuelve los datos de la pregunta hecha