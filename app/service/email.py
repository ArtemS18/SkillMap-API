from logging import getLogger
from service import pwd, exception
from smtp.client import smtp_client
from redis_client.client import get_client
from smtp.templates import verifi_email_template

from db import models


TIME_CODE_EXPIRED = 60
log = getLogger(__name__)


async def send_verify_code(email: str):
    verify_code = pwd.create_code()
    redis = get_client()
    await redis.setex(f"verify-code:{email}", TIME_CODE_EXPIRED, verify_code)
    await smtp_client.send_email(verifi_email_template(to_user=email, code=verify_code))


async def verify_email_code(email: str, code: str):
    redis = get_client()
    key = f"verify-code:{email}"
    raw: bytes = await redis.get(key)
    if raw is None:
        raise exception.InvalideVerifyCode
    verify_code = raw.decode()
    log.info(code)
    log.info(key)
    if code != verify_code:
        raise exception.InvalideVerifyCode
    res = await models.User.filter(email=email).update(email_verified=True)
    await redis.delete(key)
    if res == 0:
        raise exception.NotFoundError("user")
    return True
