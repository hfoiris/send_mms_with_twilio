import os
from twilio.rest import Client

def send_mms():
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body='I am as cute as baby yoda :)',
            media_url='https://helios-i.mashable.com/imagery/articles/06Qx8phppzGdXs2CVE7QlwP/hero-image.fill.size_1248x702.v1623391437.jpg',
            from_='+1<YOUR_TWILIO_NUMBER>',
            to='+1<TARGET_PHONE_NUMBER>'
        )

    print(message.sid)

if __name__ == '__main__':
    send_mms()