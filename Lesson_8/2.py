# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.

class OwnError(Exception):

    def __init__(self, txt):
        self.txt = txt


while True:
    try:
        inp_data = int(input("Введите целое число: "))
        if inp_data == 0:
            raise OwnError("Делить на 0 нельзя")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(100 / inp_data)
        break
