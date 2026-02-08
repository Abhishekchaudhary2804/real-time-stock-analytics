import requests

BOT_TOKEN = "8315800894:AAHTn-RuO6AgNJ7LaFW8mewE0p7vnwYxeaI"

CHAT_ID = "8315800894"

def send_alert(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url,data={"chat_id":CHAT_ID,"text":msg})
