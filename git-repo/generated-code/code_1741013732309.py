def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 10
fibonacci_sequence = list(fibonacci(n))
print(fibonacci_sequence)