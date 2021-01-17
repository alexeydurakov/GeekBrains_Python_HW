# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_for_3.txt', 'r', encoding='utf-8') as f:
    list_empl = [el.split() for el in f.readlines()]
print(list_empl)
sum = 0
for el in list_empl:
    if float(el[1]) < 20000:
        print(f'У {el[0]}а оклад {el[1]}')
    sum += float(el[1])

print(f'Cредняя величина дохода сотрудников {sum / len(list_empl):.2f}')