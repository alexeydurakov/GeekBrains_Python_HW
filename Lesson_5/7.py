# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

my_dict ={}
dict_av ={}
sum_profit =0
with open('text_for_7.txt', 'r', encoding='utf-8') as f:
    for el in f.readlines():
        count_firm = len(el.split())
        name_firm, owner, income, costs = el.split()
        profit = int(income) - int(costs)
        sum_profit += profit
        my_dict[name_firm] = profit

dict_av['average_profit'] = int(sum_profit / count_firm)
my_list = [my_dict]
my_list.append(dict_av)

with open('json_for_7.json','w') as f:
    json.dump(my_list, f)