from sys import argv
from itertools import cycle

name_script, data_list, break_num = argv

i = 0
for el in cycle(data_list):
    if i > break_num:
        break
    else:
        print(el)
        i += 1
