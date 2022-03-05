import time

number = str(1 / 55)
number = number[number.index('.') + 1:]
print(number)
current_cross_section = '1'
for place in range(1, len(number)):
    current_cross_section = number[0:place]
    print(current_cross_section)
    next_cross_section = number[len(current_cross_section):2 * len(current_cross_section)]
    print(next_cross_section)
    next_next_cross_section = number[2 * len(current_cross_section): 3 * len(current_cross_section)]
    print(next_next_cross_section)
    print(current_cross_section == next_cross_section == next_next_cross_section)
    if current_cross_section == next_cross_section == next_cross_section:
        print(current_cross_section)
        print(str(current_cross_section) + ' is the repeating decimal')
        break
print(number + ' has no repeat')
