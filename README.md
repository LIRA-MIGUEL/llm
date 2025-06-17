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