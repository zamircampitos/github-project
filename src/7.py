import random

def get_random_code():
    numbers = "23456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    special_characters = "-!@#$%^&*"
    code = ""
    for i in range(8):
        if i % 2 == 0:
            code += random.choice(letters)
        elif i % 3 == 0:
            code += random.choice(special_characters)
        else:
            code += random.choice(numbers)
    return code