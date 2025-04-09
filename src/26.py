def square_root(num):
    if num < 0:
        raise ValueError("Cannot compute square root of a negative number")
    sqrt = num ** 0.5
    return int(sqrt)

try:
    print(square_root(-4))
except ValueError as e:
    print(e)
