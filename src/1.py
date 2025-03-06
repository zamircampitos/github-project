def get_random_code():
    import random
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyz"
    symbols = "!@#$%^&*()_+-=[]{}|;':\"<>,./?`~"
    all_characters = numbers + letters + symbols
    code = ""
    for i in range(10):
        code += random.choice(all_characters)
    return code
