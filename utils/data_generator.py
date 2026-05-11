import random
import string
import time


def random_email(prefix: str = "qa_test") -> str:
    ts = int(time.time())
    suffix = "".join(random.choices(string.ascii_lowercase, k=4))
    return f"{prefix}_{ts}_{suffix}@test.com"


def random_phone() -> str:
    return "".join(random.choices(string.digits, k=10))


def random_string(length: int = 8) -> str:
    return "".join(random.choices(string.ascii_letters, k=length))