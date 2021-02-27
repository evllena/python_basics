from collections import Counter

list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
c = Counter(list1)
list2 = [el for el in list1 if c[el] == 1]
print(list2)