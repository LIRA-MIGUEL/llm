
import os
from groq import Groq

client = Groq(api_key="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")
filename = os.path.join(os.path.dirname(__file__), "vocaro.mp3")

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()),
      model="distil-whisper-large-v3-en",
      response_format="verbose_json",
    )
    print(transcription.text)
      