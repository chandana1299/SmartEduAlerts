from gtts import gTTS
import os

def generate_voice(text, lang):
    path = f"static/audio/{lang}.mp3"
    tts = gTTS(text=text, lang=lang)
    tts.save(path)
    return path
