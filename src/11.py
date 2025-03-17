import random

def generate_random_code():
    """Generates a random code"""
    code = ''
    for i in range(8):
        code += str(random.randint(0, 9))
    return code
