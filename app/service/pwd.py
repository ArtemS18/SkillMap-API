from passlib.hash import argon2
import secrets
import string


def hash_password(password: str) -> str:
    return str(argon2.hash(password))


def verifi_password(password: str, hashed_password: str) -> bool:
    return argon2.verify(password, hashed_password)


def create_code(lenght: int = 6) -> str:
    letters = string.ascii_uppercase + string.digits
    return "".join(secrets.choice(letters) for i in range(lenght))
