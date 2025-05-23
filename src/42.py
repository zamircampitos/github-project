def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_seq = [0, 1]
        for i in range(2, n + 1):
            next_fib = fib_seq[-1] + fib_seq[-2]
            fib_seq.append(next_fib)
        return fib_seq

# Example usage:
n = 10
fibonacci_seq = fibonacci(n)
print(fibonacci_seq)
