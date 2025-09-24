from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8153628719:AAECTzf8tBlrvpK3S_LPbM9w2IT24oAm2Pk"
TELEGRAM_CHAT_ID = "-1002829383667"  # رقم قناتك

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if not data:
        return "No JSON received", 400

    message = f"🚨 إشارة جديدة 🚨\n\n📊 الرمز: {data.get('symbol')}\n💵 السعر: {data.get('price')}\n🕒 الوقت: {data.get('time')}\n📈 الإشارة: {data.get('signal')}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

    return "Message sent to Telegram", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
