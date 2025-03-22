from twilio.rest import Client
from config import auth_token, account_sid, phone_number


def set_twilio_connection(account_sid, auth_token):
    
    client = Client(account_sid, auth_token)
    return client


def send_message(client, quote):
    message = client.messages.create(
                        from_='+19898188150',
                        body = quote,
                        to=phone_number,
                        )
    return message.sid

client = set_twilio_connection(account_sid, auth_token)