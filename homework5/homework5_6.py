dic = {}
with open("task6.txt", encoding='utf-8') as info:
    for line in info:
        discipline, hours = line.split(':')
        sum_hours = (sum(map(int, "".join([i for i in hours if i == ' ' or '9' >= i >= '0']).split())))
        dic[discipline] = sum_hours
print(dic)
