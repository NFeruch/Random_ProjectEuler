def fibonacci():
    fib_list = [1, 1]
    while len(str(fib_list[-1])) < 1000:
        fib_list.append(fib_list[-1] + fib_list[-2])
    fib_list.pop(0)
    return fib_list


print(fibonacci().index(fibonacci()[-1]) + 1)
