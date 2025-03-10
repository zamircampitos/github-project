import random

def generate_random_python_code():
    """Generate a random Python code."""
    # Define a list of valid Python keywords
    keywords = ['if', 'else', 'while', 'for', 'in', 'print']

    # Define a list of valid Python operators
    operators = ['+', '-', '*', '/', '%', '//', '**']

    # Define a list of valid Python identifiers
    identifiers = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]

    # Define a list of valid Python data types
    data_types = ['int', 'float', 'str', 'bool']

    # Generate a random string of Python code
    code = ''
    for _ in range(random.randint(5, 20)):
        # Choose a random keyword, operator, identifier, or data type
        choice = random.choice([keywords, operators, identifiers, data_types])

        # Append the chosen element to the code string
        code += ' ' + str(random.choice(choice))

    return code