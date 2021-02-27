from functools import reduce


def multiple(a, b):
    return a * b


list1 = [el for el in range(100, 1001) if el % 2 == 0]

print(list1)
print(reduce(multiple, list1))