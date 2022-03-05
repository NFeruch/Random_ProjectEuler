def is_even(n):
    if str(n)[-1] in '02468':
        return True
    return False


def fibonacci():
    result = 0
    fib_list = [1, 1]
    while fib_list[-1] < 4000000:
        fib_list.append(fib_list[-1] + fib_list[-2])
        if is_even(fib_list[-1]):
            result += fib_list[-1]
    return result


print(fibonacci())
