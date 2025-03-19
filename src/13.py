  import random

def get_random_python_code():
    # Generate a random number between 1 and 10
    num = random.randint(1, 10)

    # Return a string with the corresponding Python code
    if num == 1:
        return "print('Hello World!')"
    elif num == 2:
        return "for i in range(5): print(i)"
    elif num == 3:
        return "numbers = [1, 2, 3, 4, 5]"
    elif num == 4:
        return "def greet(name):"
    elif num == 5:
        return "greet('Alice')"
    elif num == 6:
        return "if __name__ == '__main__':"
    elif num == 7:
        return "import os"
    elif num == 8:
        return "os.system('date')"
    elif num == 9:
        return "a = [1, 2, 3]"
    else:
        return "b = a[1]"