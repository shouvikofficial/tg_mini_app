from flask import Flask, request, jsonify
from telegram import Bot
import os

app = Flask(__name__)

# Use your bot API token (replace with a secure method)
BOT_TOKEN = os.getenv("BOT_TOKEN", "7850249781:AAG11pOjNjHFVMVzvTK0s4Op2kcGDtmG9EM")
bot = Bot(token=BOT_TOKEN)

ADDRESS_FILE = "addresses.txt"

@app.route("/submit", methods=["POST"])
def submit_address():
    data = request.get_json()
    user_id = data.get("user_id", "unknown")
    address = data.get("address", "")

    if not address:
        return jsonify({"message": "Address is required"}), 400

    # Save address to a file
    with open(ADDRESS_FILE, "a") as file:
        file.write(f"{user_id}: {address}\n")

    # Send confirmation via Telegram
    try:
        bot.send_message(chat_id=user_id, text=f"✅ Your address has been saved: {address}")
    except Exception as e:
        print(f"Failed to send message: {e}")

    return jsonify({"message": "Address saved successfully"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
