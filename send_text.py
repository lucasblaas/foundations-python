from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACb00c3f6497c468783f0f11e21663fdac"
# Your Auth Token from twilio.com/console
auth_token  = "bd7d85e180dec9e122581b174fb93375"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5553984110187", 
    from_="+553140428326",
    body="My name is Lucas")

print(message.sid)

## problems generated because of the number in twillio. It wasn`t able to send SMS just call messages
## to fix that I delete the old number to create a new one but I wont create anymore in trial account