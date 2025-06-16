
import os
from groq import Groq
from pathlib import Path


client = Groq(api_key="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")
speech_file_path = Path(__file__).parent / "speech.wav"
response = client.audio.speech.create(
  model="playai-tts",
  voice="Aaliyah-PlayAI",
  response_format="wav",
  input="Hola como estas, me llamo juanito y soy fan de tailor swift",
)
response.write_to_file(speech_file_path)

      