from email.message import EmailMessage


def verifi_email_template(to_user: str, code: str) -> EmailMessage:
    message = EmailMessage()
    message["To"] = to_user
    message["Subject"] = "Confirm your email!"
    message.set_content(f"Your verifi code: {code}")
    return message
