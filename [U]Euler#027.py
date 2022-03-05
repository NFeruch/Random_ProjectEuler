def is_prime(value):
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def quadratic():
    largest_n = 0
    for a in range(0, 1):
        for b in range(39, 43):
            n = 0
            quadratic_equation = 2
            while is_prime(quadratic_equation):
                quadratic_equation = (n ** 2) + (a * n) + b
                n += 1
                print(n)
            if n > largest_n:
                largest_n = n
    return largest_n


print(quadratic())
