def fact_gen(num):
    fact_num = 1
    if num == 0:
        yield f"{num}! = {fact_num}."
    for el in range(1, num + 1):
        fact_num *= el
        yield f"{el}! = {fact_num}."


for el in fact_gen(int(input("Введите целое число: "))):
    print(el)