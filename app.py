from flask import Flask, request
import requests

app= Flask(_name_)

TOKEN ="8632587398:AAGnaRtWzU4ZWFuGuZlVaNMQIgdAoYeI8eE"
CHAT = "5950286852"

def send_msg(msg):
    url ="https://api.telegram.org/bot" + TOKEN + "/sendMessage"
    requests.post(url, json={"chat_id": CHAT "text": msg})

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(silent=True) or {}
    action = data.get("action", "UNKNOWN")
    symbol = data.get("symbol", "UNKNOWN")
    send_msg("ALERT! Action: " + action + " Symbol: " + symbol
    return "OK", 200
    if _name_ ="_main_":
    app.run(host="0.0.0.0", port=5000)
