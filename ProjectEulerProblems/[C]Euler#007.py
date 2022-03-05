def is_prime(value):
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def primes_list(value):
    primes = []
    test_num = 2
    while len(primes) <= value - 1:
        if is_prime(test_num):
            primes.append(test_num)
            print(str(test_num) + ' is the ' + str(primes.index(test_num) + 1) + 'th prime')
        test_num += 1
    # return primes[value - 1]


print(primes_list(10001))
