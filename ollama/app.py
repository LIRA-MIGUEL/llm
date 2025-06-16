from groq import Groq

client = Groq(api_key="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")

completion = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": "¿Cuál es la capital de Japón?"  # ✅ Asegúrate de que esto no esté vacío
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False
)

print(completion.choices[0].message.content)
