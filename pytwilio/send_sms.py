from twilio.rest import Client

account_sid = "AC50dd941412396ebf737fdf98ddb3720f"
auth_token = "880c6e45d6e972aa83c2953f944904f9"

client = Client(account_sid, auth_token)

client.messages.create(
    to = "+17315923281",
    from_ = "+12702165035",
    body = "CENTSense here! We just wanted to remind you that your income
    will be split between savings (20%) and charity (10%) in a few days."
)
