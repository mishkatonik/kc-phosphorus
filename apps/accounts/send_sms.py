import os
from twilio.rest import Client


account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

client.messages.create(
    from_="+15035738748",
    to='+19259147475',
    body="Today's Phosphorus Forecast", 
)

