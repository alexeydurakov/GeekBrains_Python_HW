# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name_script, work_hours, rate_hour, premium = argv


def calc_empl_salary(wh, rh, pr):
    return (float(wh) * float(rh)) + float(pr)


print(calc_empl_salary(work_hours, rate_hour, premium))
