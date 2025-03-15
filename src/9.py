import random

def get_random_code(length=8):
    letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(random.choice(letters) for _ in range(length))

# Example usage:
print(get_random_code())