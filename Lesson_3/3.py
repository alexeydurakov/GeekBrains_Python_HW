# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(*args):

    if args[0] >= args[1] >= args[2]:
        sum = args[0] + args[1]
    elif args[0] <= args[1] <= args[2]:
        sum = args[1] + args[2]
    elif args[0] <= args[2] <= args[1]:
        sum = args[2] + args[1]
    return sum


print(my_func(2, 3, 4))
