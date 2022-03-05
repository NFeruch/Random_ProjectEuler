largest_palindrome = 0
for first_multiplier in range(100, 1000):
    for second_multiplier in range(100, 1000):

        current_product = str(first_multiplier * second_multiplier)
        if len(current_product) == 5:
            if current_product[0] == current_product[4] and current_product[1] == current_product[3]:
                if int(current_product) > int(largest_palindrome):
                    largest_palindrome = current_product

        if len(current_product) == 6:
            if current_product[0] == current_product[5] and current_product[1] == current_product[4] \
                    and current_product[2] == current_product[3]:
                if int(current_product) > int(largest_palindrome):
                    largest_palindrome = current_product

print(largest_palindrome)
