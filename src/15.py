import numpy as np

def generate_random_matrix(rows, cols):
    """
    Generate a random matrix with specified dimensions.
    
    Args:
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.
        
    Returns:
        np.ndarray: A randomly generated square matrix of size (rows, cols).
    """
    # Seed for reproducible results
    np.random.seed(42)
    
    # Generate random numbers to create a matrix with random values
    matrix = np.random.rand(rows, cols)  # Example matrix with float values between 0 and 1
    
    return matrix

# Example usage:
random_matrix = generate_random_matrix(3, 3)
print(random_matrix)
