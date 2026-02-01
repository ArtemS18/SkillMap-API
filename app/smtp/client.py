import logging
from aiosmtplib import SMTP
from email.message import EmailMessage

logger = logging.getLogger(__name__)


class SMTPAccessor:
    def __init__(self, host: str, port: int, tls: bool = False):
        self.root_email = "awesome@email.com"
        self.host = host
        self.port = port
        self.tls = tls

    async def get_connect(self) -> SMTP:
        client = SMTP(hostname=self.host, port=self.port, start_tls=self.tls)
        await client.connect()
        return client

    async def send_email(self, msg: EmailMessage):
        msg["From"] = msg.get("From", self.root_email)
        client = await self.get_connect()
        async with client:
            await client.send_message(msg)
            logger.info(f"Send message from {self.root_email}")


smtp_client = SMTPAccessor("localhost", 1025)
