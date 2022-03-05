def is_even(n):
    if str(n)[-1] in ('0', '2', '4', '6', '8'):
        return True
    return False


def collatz(n):
    chain_list = [n]
    while n != 1:
        if is_even(n):
            n = int(n / 2)
        else:
            n = 3*n + 1
        chain_list.append(n)
    return chain_list


def length_of_collatz_chain(value):
    length = []
    # length[0] == 2
    for i in range(2, value):
        length.append(len(collatz(i)))
        print(len(length))
        print(length.index(max(length)))
    return length[length.index(max(length))]


print(len(collatz(837799)))
# print(length_of_collatz_chain(1000000))
