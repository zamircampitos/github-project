import numpy as np

def calculate_factorial(n):
    """
    Calculate the factorial of a number n.
    
    Parameters:
    - n: A non-negative integer
    
    Returns:
    - The factorial of n
    """
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1)

# Example usage
n = 5
result = calculate_factorial(n)
print(f"The factorial of {n} is: {result}")
