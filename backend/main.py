from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io
from groq import Groq

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia esto a tus dominios si es necesario
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key="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")

df_cache = None

@app.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...)):
    global df_cache
    try:
        contents = await file.read()
        df_cache = pd.read_csv(io.BytesIO(contents))
        return {"message": "Archivo CSV cargado correctamente"}
    except Exception as e:
        return {"error": f"Error al procesar el archivo CSV: {str(e)}"}

@app.post("/preguntar/")
async def preguntar(pregunta: str = Form(...)):
    global df_cache
    if df_cache is None:
        return {"error": "No se ha subido un archivo CSV aún"}

    try:
        # Limitamos la tabla para no pasar demasiados datos al prompt
        contexto = df_cache.head(10).to_string(index=False)
        prompt = f"""
Tengo la siguiente tabla (primeras filas):

{contexto}

Pregunta: {pregunta}
Responde como un analista de datos profesional, con precisión y claridad.
"""

        chat = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
        )
        respuesta = chat.choices[0].message.content
        return {"respuesta": respuesta}
    except Exception as e:
        return {"error": f"Error al procesar la pregunta: {str(e)}"}
