import math

def calculate_pi():
    """
    Calculate pi using an approximation method.
    """
    # Define the approximation of pi
    approx_pi = 4.0 / (1 + 3.0 / 5.0)

    return approx_pi

# Example usage:
pi_value = calculate_pi()
print(f"Calculated Pi value: {pi_value:.6f}")
