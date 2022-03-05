def factorial(n):  # 4! == 24
    result = n
    for i in range(1, n):
        result *= n - i
    return result


factorial = factorial(100)
numbers_summed = 0
for number in str(factorial):
    numbers_summed += int(number)

print(numbers_summed)
