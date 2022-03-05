def is_prime(n):
    if n in [0, 1]:
        return False
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    return True


def largest_prime(number_to_reach):
    largest_prime_num = 0
    current_num = 3
    while number_to_reach > 1:
        if is_prime(current_num) and number_to_reach % current_num == 0:
            largest_prime_num = current_num
            number_to_reach //= current_num
        current_num += 2
    return largest_prime_num


print(largest_prime(600851475143))
