def is_prime(value):
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def factorial(n):
    result = n
    for i in range(1, n):
        result *= n - i
    return result


def is_even(n):
    if str(n)[-1] in '02468':
        return True
    return False


def get_factors(n):
    factors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            if n < 0:
                factors.append(i)
                factors.append(-i)
            else:
                factors.append(i)
                if n == i ** 2:
                    factors.append(i)
    return factors



