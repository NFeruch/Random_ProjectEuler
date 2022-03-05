def result(value):
    square_then_sum = 0
    sum_then_square = 0
    for i in range(1, value + 1):
        square_then_sum += i**2
        sum_then_square += i
    return sum_then_square**2 - square_then_sum


print(result(100))
