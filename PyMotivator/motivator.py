
import requests
from twilio_conn import send_message,client


url = "https://zenquotes.io/api/random"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    quote = data[0]["q"]  # Extract only the quote
    print(quote)
else:
    print(f"Error: {res.status_code}")


send_message(client, quote)