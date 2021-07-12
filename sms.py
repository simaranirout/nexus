# # Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = 'AC13d3903dfde9765112ef41402125dbe2'
# auth_token = 'c9e0ec043a5a84499e372fd28853b88b'
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                     body="HAPPY NEW YEAR 2021",
#                     from_='+12055372319',
#                     to='+918280306218'
#                 )

# print(message.sid)
import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization": "lrxc2LDzYIUQomsREiMnJKO0Zp36fh9bXdHaj7NqA5guyTC1eviRFZsn8PCkagJVOhfHSTjAzUdxcwlm",
               "sender_id": "FSTSMS",
               "message": "(FROM:-SIMARANI ROUT) The new year begins, let us pray,It will be a year with a new peace, New happiness,& the abundance of friends,God bless you through out the new year.. Happy New Year 2021 :)",
               "language": "english",
               "route": "p",
               "numbers": "8249835362,7064723361,7262996041,6371506917,7008824700,7064473585"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
