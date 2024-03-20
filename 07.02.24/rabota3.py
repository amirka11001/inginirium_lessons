from itertools import  chain
from itertools import groupby

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = [7, 8, 9]

for i in chain(list_a, list_b, list_c):
    if i == 14:
        print("Найдено")

for key, group in groupby('kljdfb'):
    print(key, list(group))