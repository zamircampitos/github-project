import random

def get_random_code():
    code = "".join(random.choice("1234567890abcdef") for i in range(8))
    return code
