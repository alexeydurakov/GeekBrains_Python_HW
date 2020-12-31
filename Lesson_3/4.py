# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    sum = 1
    for i in range(1, abs(y) +1):
        sum *= x
    return 1 / sum


base_num = float(input('Введите действительное положительное число: '))
degree_num = int(input('Введите целое отрицательное число :'))

print(f'Искомое число {my_func_1(base_num, degree_num)}')
print(f'Искомое число {my_func_2(base_num, degree_num)}')
