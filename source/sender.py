
import os
from flask import Flask, request,redirect

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
print(f"account_sid: {account_sid}\nauth_token: {auth_token}")
Client = Client(account_sid,auth_token)

from_Whatsapp ='whatsapp:'+str(os.getenv('FROM_NUMBER'))
to_Whatsapp="whatsapp:"+str(os.getenv('TO_NUMBER'))

Client.messages.create(
    body="Hello World",
    from_=from_Whatsapp,
    to=to_Whatsapp
)

app=Flask(__name__)
@app.route('/whatsapp', methods=['POST'])
def reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Hello, thanks for the message!")

    return str(resp)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
    # Client.messages.create(
    #     body="Hello World",
    #     from_=from_Whatsapp,
    #     to=to_Whatsapp
    # )