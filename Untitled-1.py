def sum_even_numbers(numbers):
    sum_even = 0
    for num in numbers:
        if num % 2 == 0:
            sum_even += num
    return sum_even
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
result = sum_even_numbers(num_list)
print("Sum of even numbers:", result)