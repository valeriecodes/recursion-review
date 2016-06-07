def fibonacci(n):
    fibonacci_nums = [0, 1]
    while len(fibonacci_nums) <= n:
        fibonacci_nums.append(fibonacci_nums[-2] + fibonacci_nums[-1])
    return fibonacci_nums[-1]

print fibonacci(6)
