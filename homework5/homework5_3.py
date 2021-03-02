with open("task3.txt", "r", encoding='utf-8') as f:
    salary_dic = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f"Средняя зарплата сотрудников составляет {round(sum(salary_dic.values())/len(salary_dic))} рублей.")
    print(f"Меньше 20000 получают сотрудники: {[a[0] for a in salary_dic.items() if a[1] < 20000]}")

