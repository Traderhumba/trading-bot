
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    This endpoint receives POST requests from TradingView webhooks.
    The body of the request should be JSON formatted.
    """
    try:
        data = request.get_json(force=True)
        print("Received alert:", data)

        # Example: basic handling logic
        if data and 'ticker' in data:
            print(f"Alert for {data['ticker']} triggered!")
            # You can connect your trading logic here, e.g., send order API call

        return jsonify({"status": "success", "message": "Alert received"}), 200

    except Exception as e:
        print("Error occurred:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "TradingView Webhook Bot is running."}), 200


if __name__ == '__main__':
    # Host 0.0.0.0 allows external services (like ngrok) to connect
    app.run(host='0.0.0.0', port=5000)
