rus_num = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text04.txt", "w", encoding='utf-8') as result:
    with open("task4.txt", encoding='utf-8') as initial:
        result.writelines([line.replace(line.split()[0], rus_num.get(line.split()[0])) for line in initial])
