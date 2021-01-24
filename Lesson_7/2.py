# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название.
#
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
#
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param


    @property
    def calc_expense_textil(self):
        return (self.param / 6.5 + 0.5) + (2 * self.param + 0.3)

    @abstractmethod
    def my_method(self):
        return 'абстрактый метод в классе Clothes'


class Coat(Clothes):
    def calc_expense_textil(self):
        return (self.param / 6.5 + 0.5)

    def my_method(self):
        return 'вызов абстрактного метода в классе Coat'


class Suit(Clothes):
    def calc_expense_textil(self):
        return (2 * self.param + 0.3)

    def my_method(self):
        return 'вызов абстрактного метода в классе Suit'

c = Coat(650)
s = Suit(40)
print(c.calc_expense_textil())
print(s.calc_expense_textil())
print(c.my_method())
print(s.my_method())