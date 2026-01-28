from flask import Flask, render_template, request
import time

from modules.parser import parse_file
from modules.ml_predictor import predict_alert
from modules.translator import translate_text
from modules.tts import generate_voice
from modules.telegram_bot import send_text, send_voice
from config import LANGUAGES

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        students = parse_file(file)

        for s in students:
            prediction = predict_alert(s)

            if prediction == 1:
                base_msg = (
                    f"Dear Parent, your ward {s['name']} "
                    f"requires immediate attention regarding attendance or fees."
                )

                # Send TEXT alerts in multiple languages
                for lang in LANGUAGES:
                    translated = translate_text(base_msg, lang)
                    send_text(s["chat_id"], translated)
                    time.sleep(0.5)   # Prevent Telegram throttling

                # Send VOICE alert only once (English)
                audio = generate_voice(base_msg, "en")
                send_voice(s["chat_id"], audio)
                time.sleep(1)

        return " Alerts successfully sent! Please check Telegram."

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=False)
