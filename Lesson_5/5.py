# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

# генераторс строки случайных целых чисел
num_list = []
num = random.randint(1, 100)
num_list = [str(random.randint(1, el)) for el in range(1, num)]

# преобразование списка в строку
wr_list = ' '.join(num_list)

# #создание и запись в файл
with open('text_for_5.txt', 'w') as f:
    f.writelines(wr_list)
#чтение из файла строки
with open('text_for_5.txt', 'r') as f:
    sum_list = f.readline().split()

print(sum(map(int, sum_list)))