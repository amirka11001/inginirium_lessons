from itertools import product

list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9, 10]
list_c = [11, 12, 13, 14, 15]

for a, b, c in product(list_a, list_b, list_c):
    if a + b + c == 23:
        print(a, b, c)