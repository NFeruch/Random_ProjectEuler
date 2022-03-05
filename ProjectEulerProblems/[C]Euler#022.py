with open(r"C:\Users\user\Desktop\ProjectEuler\p022_names.txt", 'r', encoding='utf-8') as f:
    names = f.read()
names = names.replace('"', '')
names_list = names.split(',')
names_list.sort()
print(names_list)

alphabet = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
            'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
            'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
            'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def names_score():
    all_names_score = 0
    for name in names_list:
        current_name_score = 0
        for letter in name:
            current_name_score += alphabet[letter]
        all_names_score += (current_name_score * (names_list.index(name) + 1))
    return all_names_score


print(names_score())
