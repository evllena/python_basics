import json

my_list = []
sum_profit = 0
sum_f = 0
sum_damage = 0
dam_f = 0
with open("task7.json", "w", encoding='utf-8') as new_file:
    with open("task7.txt", encoding='utf-8') as init_file:
        for line in init_file:
            revenue, costs = map(float, (line.split()[1], line.split()[2]))
            profit = revenue - costs
            if profit > 0:
                sum_profit += profit
                sum_f += 1
            else:
                sum_damage += profit
                dam_f += 1
            dic_res = {line.split()[0]: profit}
            my_list.append(dic_res)
        my_list.append({"average profit": round(sum_profit / sum_f)})
        my_list.append({"average damage": round(sum_damage / dam_f)})
    json.dump(my_list, new_file)
print(my_list)
