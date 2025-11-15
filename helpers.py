# helpers.py
import random
from data import TestDATA


class Helper:
    @staticmethod
    def random_email() -> str:
        """Генерирует рандомный email под заданный префикс и домен."""
        number = random.randint(1000, 9999)
        return f"{TestDATA.RANDOM_EMAIL_PREFIX}{number}@{TestDATA.RANDOM_EMAIL_DOMAIN}"
