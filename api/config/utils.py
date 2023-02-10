import random
import string


def randomStrig(num: int) -> string:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num))
