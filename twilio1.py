from twilio.rest import Client
account_sid =  "ACb57c456d605645f2aef0aa3da87729fc"
auth_token  = "8ba89c04e01844f6b1edb0d0c498f12f"
client =  Client(account_sid,auth_token)
message = client.messages.create(to= "+917725954755",
                                from_ = "+15038502549",
                                body = "HY I AM GAUTAMI SHARMA,NICE TO MEET YOU")

print(message.sid)