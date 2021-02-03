# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных
# экземпляров.
# Проверьте корректность полученного результата.

class Complex_number():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        x = complex(self.a, self.b)
        y = complex(other.a, other.b)
        return f'Сумма равна: {x + y}'

    def __mul__(self, other):
        x = complex(self.a, self.b)
        y = complex(other.a, other.b)
        return f'Произведение равно: {x * y}'

compl_1 = Complex_number(1, 2)
compl_2 = Complex_number(3, 4)

print(compl_1 + compl_2)
print(compl_1 * compl_2)
