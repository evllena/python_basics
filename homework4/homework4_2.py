my_list = [28, 14, 99, 23, 45, 63, 100, 36, 49, 90, 70, 94, 71, 89, 1, 13]
new_list = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(new_list)