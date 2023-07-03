def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result
number = 5
factorial_result = factorial(number)
if factorial_result is not None:
    print("Factorial of", number, "is:", factorial_result)
else:
    print("Factorial of a negative number is undefined.")
