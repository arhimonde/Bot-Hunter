import requests

def send_telegram_alert(bot_token, chat_id, message):
    """
    Sends a message to a Telegram chat using a bot token via the Telegram Bot API.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    
    payload = {
        "chat_id": chat_id,
        "text": message
    }
    
    try:
        response = requests.post(url, json=payload)
        
        # Raise an exception if the request returned an unsuccessful status code
        response.raise_for_status()
        
        print("Telegram alert sent successfully.")
        return response.json()
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while sending Telegram alert: {http_err}")
        print(f"Response: {response.text}") # Detailed error from Telegram
    except Exception as err:
        print(f"An error occurred while sending Telegram alert: {err}")
    
    return None

if __name__ == "__main__":
    # Test block (placeholder values)
    # send_telegram_alert("YOUR_TOKEN", "YOUR_CHAT_ID", "Price Tracker Test Message")
    pass
