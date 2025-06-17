from groq import Groq

client = Groq(api_key="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")
completion = client.chat.completions.create(
    model="deepseek-r1-distill-llama-70b",
    messages=[
        {
            "role": "system",
            "content": "Eres un asistente útil, claro y conciso. Responde como si fueras un experto en tecnología."
        },
        {
            "role": "user",
            "content": "¿Cuál es la diferencia entre la inteligencia artificial débil y fuerte?"
        }
    ],
    temperature=0.7,              
    max_completion_tokens=1024,   
    top_p=0.9,                    
    stream=True,                  
    stop=None                     
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
