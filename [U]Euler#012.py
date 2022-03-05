def get_factors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors


def nth_triangle_number(n):
    current_triangle_num = 0
    for i in range(1, n + 1):
        current_triangle_num += i
    return current_triangle_num


count = 1
number_of_divisors = 1
while number_of_divisors <= 500:
    number_of_divisors = len(get_factors(nth_triangle_number(count)))
    print(nth_triangle_number(count))
    count += 1
print(get_factors(nth_triangle_number(count - 1)))
