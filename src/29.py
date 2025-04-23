import math
from decimal import Decimal

def calculate_discount(price, discount_percentage):
    """
    Calculate the final price after applying a discount.
    
    Parameters:
    - price: The original price of an item.
    - discount_percentage: The percentage off the original price to be applied.
    
    Returns:
    - The final price after discount.
    """
    discount_amount = Decimal(price) * Decimal(discount_percentage)/100
    final_price = price - discount_amount
    return final_price

# Example usage and test cases:
original_price = 10.50
discount_percentage = 20
final_price = calculate_discount(original_price, discount_percentage)
print(f"The final price after applying the discount is: {final_price}")
