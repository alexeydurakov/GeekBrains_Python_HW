# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

trans_dic = {'1':'Один', '2':'Два', '3':'Три', '4':'Четыре'}
new_str = ''
with open('text_for_4.txt', 'r', encoding='utf-8') as f:
    for el in f:
        elem = el.split()
        elem[0] = trans_dic.get(elem[2])
        el_str = ' '.join(elem)
        new_str = new_str + el_str + '\n'

print(new_str)

with open('text_for_4.txt', 'w',encoding='utf-8') as f:
    f.write(new_str)

