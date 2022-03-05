def smallest_multiple(upper_bound):
    result = 0
    current_number = 1
    while result == 0:
        for i in range(1, upper_bound + 1):
            if current_number % i != 0:
                break
            elif i == upper_bound:
                result = current_number
        print(current_number)
        current_number += 1
    return result


print(smallest_multiple(20))
