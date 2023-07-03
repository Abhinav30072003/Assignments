def fibonacci(n):
    fib_series = []
    if n <= 0:
        return fib_series
    fib_series.append(0)  
    if n == 1:
        return fib_series
    fib_series.append(1)
    if n == 2:
        return fib_series
    for i in range(2, n):
        next_num = fib_series[i-1] + fib_series[i-2]
        fib_series.append(next_num)
    return fib_series

num_terms = 10
fibonacci_series = fibonacci(num_terms)
print("Fibonacci series:")
for term in fibonacci_series:
    print(term, end=" ")