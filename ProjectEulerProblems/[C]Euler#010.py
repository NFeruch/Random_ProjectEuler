import timeit
start = timeit.default_timer()


def is_prime(value):
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def sum_of_primes(target):
    result = 2
    for i in range(3, target, 2):
        if is_prime(i):
            print(i)
            result += i
    return result


print(sum_of_primes(2000000))

stop = timeit.default_timer()
print('Time: ', stop - start)
