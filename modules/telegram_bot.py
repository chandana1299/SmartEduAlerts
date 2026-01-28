import requests
from config import BOT_TOKEN

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send_text(chat_id, message):
    try:
        requests.post(
            f"{BASE_URL}/sendMessage",
            data={"chat_id": chat_id, "text": message},
            timeout=10   # IMPORTANT
        )
    except requests.exceptions.RequestException as e:
        print(f"[Telegram Text Error] {e}")

def send_voice(chat_id, audio_path):
    try:
        with open(audio_path, "rb") as f:
            requests.post(
                f"{BASE_URL}/sendVoice",
                data={"chat_id": chat_id},
                files={"voice": f},
                timeout=20   # IMPORTANT (voice takes longer)
            )
    except requests.exceptions.RequestException as e:
        print(f"[Telegram Voice Error] {e}")
