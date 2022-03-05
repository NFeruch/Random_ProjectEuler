def result(upper):
    value = 0
    for i in range(1, upper):
        if i % 3 == 0 or i % 5 == 0:
            value += i
    return value


print(result(1000))
