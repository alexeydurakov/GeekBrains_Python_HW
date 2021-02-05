# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Data():
    def __init__(self, dmy):
        self.dmy = str(dmy)

    @classmethod
    def change_string_number(cls, dmy):
        dd, mm, yy = dmy.split('-')
        return int(dd), int(mm), int(yy)

    @staticmethod
    def valid_data(dd, mm, yy):
        if 1 <= dd <= 31 and 1 <= mm <= 12 and len(str(yy)) == 4:
            return True
        else:
            return False


dmy = input('Введите дату в формате  «день-месяц-год»: ')
t = Data(dmy)

d, m, y = t.change_string_number(dmy)
print(f'День {d}, Месяц {m}, Год {y}')
print(Data.valid_data(d, m, y))
