from twilio.rest import Client

account_sid = "AC5791a2d86be0252e5b6e8694ef387ee6"
auth_token = "357b1976cfd256b37ca43313aabe5c8f"

client = Client(account_sid,auth_token)

my_num = "+15149699306"
twilio_num = "+15796000924"

client.messages.create(
    to = my_num,
    from_ = twilio_num,
    body = "You need help"
)
