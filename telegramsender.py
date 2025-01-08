import requests

API_URL = input("Enter your API URL: ")
BOT_TOKEN = input("Enter your Bot Token: ")
CHAT_ID = input("Enter your Chat ID: ")


IMAGE_URL = "https://youreimagelinkhere.com" 
CAPTION = "HELLO SIGMA !"

def send_image():
    try:
        print("Downloading the image...")
        response = requests.get(IMAGE_URL)
        if response.status_code == 200:
            image_data = response.content
        else:
            print(f"Failed to download the image. Error: {response.text}")
            return

        print("Sending the image to Telegram...")
        payload = {
            "chat_id": CHAT_ID,
            "caption": CAPTION
        }
        files = {
            "photo": ("image.png", image_data)
        }
        telegram_response = requests.post(API_URL, data=payload, files=files)

        if telegram_response.status_code == 200:
            print("The message has been sent!")
        else:
            print(f"Failed to send the message. Error: {telegram_response.text}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    for i in range(50):
        print(f"Sending message {i + 1} of 50...")
        send_image()
