# 1 Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [
    123, 75.6, 3 + 5.5j, 'Vtdr', [12, 'odsl;s;', 789],
    ('о', 'б', 'ы', 'ч', 'н', 'а'), {1, 2, 3, 4}, frozenset({'r', 'a', 'b'}),
    {"key_1": 500, "key_2": 4}, True, b'\xd1\x82\xd0\xb5\xd0\xba\xd1\x81\xd1\x82',
    bytearray(b'some text'), None
]

for i in my_list:
    print(type(i))

# 2 Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().



def swap_elements(ml):
    j = 0
    for i in range(int(len(ml) / 2)):
        ml[j], ml[j + 1] = ml[j + 1], ml[j]
        j += 2
    return ml


my_list = []
menu = '1. Ввести данные\n2. Поменять пары элементов списка с соседним значением\n3. Выход'
while True:

    print(menu)
    change = input('Выберите пункт меню: ')

    if change == '1':
        n = int(input('Сколько элементов списка вы будете вводить(не меньше 4-х): '))
        for n in range(0, n):
            element = input(f'Введите {n + 1} - й элемент')
            my_list.append(element)
        print('Ваш список:', my_list)
    elif change == '2':
        if len(my_list) < 4:
            print('Список слишком короткий, введите еще элемент списка')
        else:
            print(swap_elements(my_list))

    elif change == '3':
        break

    else:
        print('Повторите ввод!')

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

list_season = ['Зима', 'Весна', 'Лето', 'Осень']
dict_season = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}

n_month = int(input('Введите месяц в виде целого числа от 1 до 12: '))

if n_month == 12 or n_month == 1 or n_month == 2:
    print(list_season[0])
elif n_month == 3 or n_month == 4 or n_month == 5:
    print(list_season[1])
elif n_month == 6 or n_month == 7 or n_month == 8:
    print(list_season[2])
else:
    print(list_season[3])

name_season = dict_season.keys()
for i in name_season:
    num_mon = dict_season[i]
    if n_month in num_mon:
        print(i)
        break

# 4 Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

string_words = input('Ведите строку из нескольких слов, разделённых пробелами: ')
list_words = string_words.split()
for ind, el in enumerate(list_words):
    if len(el) < 10:
        print(ind + 1, el)
    else:
        print(ind + 1, el[:10])

# 5 Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(f"Первоночальный список: {my_list}")

menu = '1. Ввести данные\n2. Выход'
while True:
    print(menu)
    change = input('Выберите пункт меню: ')

    if change == '1':
        numb = int(input("Введите целое число: "))
        for i in range(len(my_list)):

            if i < len(my_list) - 1:

                if my_list[i] == numb:
                    my_list.insert(i + 1, numb)
                    break
                elif my_list[i] > numb > my_list[i + 1]:
                    my_list.insert(i + 1, numb)
                    break
                elif my_list[i] < numb:
                    my_list.insert(i, numb)
                    break

            elif i == len(my_list) - 1 and my_list[i] > numb:
                my_list.append(numb)

        print(f'Новый рейтинг: {my_list}')
    elif change == '2':
        break


# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента —
# номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct


name_ = 'наименование'
price_ = 'цена'
count_ = 'количество'
units_ = 'единица измерения'

all_data = []
count = 1
menu = '1. Ввести данные\n2. Выход'
while True:
    print(menu)
    change = input('Выберите пункт меню: ')
    list_for_tuple = []
    dict_for_date = {}
    if change == '1':

        name_product = input('Введите наименование товара: ')
        list_for_dict = [name_, name_product]
        dict_for_date.update(Convert(list_for_dict))

        price_product = float(input('Введите цену товара: '))
        list_for_dict = [price_, price_product]
        dict_for_date.update(Convert(list_for_dict))

        count_product = int(input('Введите количество товара: '))
        list_for_dict = [count_, count_product]
        dict_for_date.update(Convert(list_for_dict))

        units_product = input('Введите единицу измерения товара: ')
        list_for_dict = [units_, units_product]
        dict_for_date.update(Convert(list_for_dict))

        list_for_tuple.append(count)
        list_for_tuple.append(dict_for_date)
        # Преобразовывам в кортеж
        all_data.append(tuple(list_for_tuple))
        print(all_data)

        count += 1

    elif change == '2':
        break
#


list_prod = []
list_price = []
list_count = []
list_unit = []
all_dict = {}
for i in range(0, len(all_data)):
    list_prom = all_data[i][1]

    list_keys = list_prom.keys()

    list_prod.append(list_prom.get("название"))
    list_price.append(list_prom.get("цена"))
    list_count.append(list_prom.get("количество"))
    list_unit.append(list_prom.get("eд"))

list_prod_property = ["название", list_prod]
dict_prod_property = Convert(list_prod_property)
all_dict.update(dict_prod_property)

list_price_property = ["цена", list_price]
dict_price_property = Convert(list_price_property)
all_dict.update(dict_price_property)

list_count_property = ["количество", list_count]
dict_count_property = Convert(list_count_property)
all_dict.update(dict_count_property)

list_unit_property = ["eд", list_unit]
dict_unit_property = Convert(list_unit_property)
all_dict.update(dict_unit_property)

print(all_dict)
