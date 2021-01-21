# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'Машина {self.name} поехала'

    def stop(self):
        return f'Машина {self.name} остановилась'

    def turn(self, direction):
        return f'Машина {self.name} повернула {direction}'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Превышение скорости: {self.speed}'
        else:
            return f'Скорость не превышена'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Превышение скорости: {self.speed}'
        else:
            return f'Скорость не превышена'


class PoliceCar(Car):
    pass


t_car = TownCar(200, 'black', 'Car_for_Town', False)
print(t_car.go(), t_car.show_speed(), t_car.turn('в право'), t_car.stop())
s_car = SportCar(400, 'rad', 'Car_for_Sport', False)
print(s_car.go(), s_car.show_speed(), s_car.turn('в право'), s_car.stop())
w_car = WorkCar(120, 'grey', 'Car_for_Work', False)
print(w_car.go(), w_car.show_speed(), w_car.turn('в лево'), w_car.stop())
p_car = PoliceCar(300, 'blue', 'Car_for_Police', True)
print(p_car.go(), p_car.show_speed(), p_car.turn('в лево'), p_car.stop())


