def square_root(x):
    if x >= 0:
        root = math.sqrt(x)
    else:
        raise ValueError("x should be non-negative.")
    return root
