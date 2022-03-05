def sum_factors(n):
    result = 0
    for i in range(1, n):
        if n % i == 0:
            result += i
    return result


def amicable_numbers():
    result = 0
    current_number = 1
    amicable = [[None, None]]
    while current_number < 10000:
        print(current_number)
        if current_number in amicable[-1]:
            current_number += 1
            continue
        else:
            first_num = sum_factors(current_number)
            second_num = sum_factors(sum_factors(current_number))
            if second_num == current_number and current_number != first_num:
                result += current_number
                result += first_num
                amicable.append([current_number, first_num])
            current_number += 1
    amicable.pop(0)
    return result, amicable


print(amicable_numbers())
