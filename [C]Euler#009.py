def pythagorean_triplets():
    for a in range(1, 1000):
        for b in range(1, 1000):
            for c in range(1, 1000):
                if a ** 2 + b ** 2 == c ** 2:
                    print(a, b, c)
                    if a + b + c == 1000:
                        print(a*b*c)
                        quit()


pythagorean_triplets()
