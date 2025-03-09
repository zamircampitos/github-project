import random

def generate_random_python_code():
    """Generates a random Python code"""
    # Generate a random integer between 1 and 10
    num = random.randint(1, 10)

    # Generate a random operator (either +, -, *, /, or %)
    op = random.choice(['+', '-', '*', '/', '%'])

    # Generate two more random integers
    num2 = random.randint(1, 10)
    num3 = random.randint(1, 10)

    # Evaluate the expression using eval() function
    result = eval(f"{num} {op} {num2} {op} {num3}")

    # Return the result as a string
    return str(result)

# Test the function with different inputs
print(generate_random_python_code())
print(generate_random_python_code())
print(generate_random_python_code())