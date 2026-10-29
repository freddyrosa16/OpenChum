import os
import requests
from dotenv import load_dotenv

load_dotenv()
my_token = os.getenv("Open_Chum_Bot_token")



def getUpdates():
    result = requests.get(f"https://api.telegram.org/bot{my_token}/getUpdates")
    if result.status_code == 200:
        data = result.json()
        chat_id = data["result"][0]["message"]["chat"]["id"]
        chat_text = data["result"][0]["message"]["text"]
        return chat_id, chat_text

def sendMessage(chat_id, chat_text):
    chat_dict = {"chat_id": chat_id, "text": chat_text}
    response = requests.post(f"https://api.telegram.org/bot{my_token}/sendMessage", json=chat_dict)


getUpdates()
sendMessage(chat_id, chat_text)
