import num2words as n2w

total = 0
for number in range(1, 1001):
    current = n2w.num2words(number).replace(' ', '')
    current = current.replace('-', '')
    total += len(current)

print(total)
