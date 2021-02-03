# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Warehouse():
    def __init__(self, quantity):
        self.quantity = quantity

    @classmethod
    def receiving_warehouse(cls, item):
        list_technics = []
        while True:
            yn = input('занести в список y или n :')
            if yn.lower() == 'y':
                try:
                    unique_name = input('Введите тип оргтехники')
                    brand_name = input('Введите производителя: ')
                    price = int(input('Введите цену за ед: '))
                    quantity = int(input('Введите количество: '))
                    inventory_number = input('Присвойте инветарный номер')
                    item = {'тип оргтехники': unique_name, 'производитель': brand_name,
                            'цену за ед': price, 'количество': quantity,
                            'инветарный номер': inventory_number}
                    item.update(item)
                    list_technics.append(item)
                except ValueError:
                    print('Недопустимое значение!')
            else:
                break
        return list_technics

    @classmethod
    def transfer_to_department(cls, list_tech):
        list_type = []
        type_technics = input('Введите тип необходимой вам техники (printer, scanner, xerox): ')
        for i in range(len(list_tech)):
            unique_name = list_tech[i][list(list_tech[i].keys())[0]]
            brand_name = list_tech[i][list(list_tech[i].keys())[1]]
            price = list_tech[i][list(list_tech[i].keys())[2]]
            quantity = list_tech[i][list(list_tech[i].keys())[3]]
            inventory_number = list_tech[i][list(list_tech[i].keys())[4]]
            prom_list = [unique_name, brand_name, price, quantity, inventory_number]
            if type_technics == unique_name:
                list_type.append(prom_list)
                print('На складе есть: ')
                print(f'{unique_name} производителя {brand_name} по цене {price}, количество {quantity}, инвентарный номер {inventory_number}')

        inv_num = input('Введите инвентарный номер нужной вам техники: ')
        for i in list_type:
            if i[4] == inv_num:
                unique_name, brand_name, price, quantity, inventory_number = i

        return unique_name, brand_name, price, quantity, inventory_number


class Office_equipment():

    def __init__(self, brand_name, price, inventory_number):
        self.brand_name = brand_name
        self.price = price
        self.inventory_number = inventory_number


class Printer(Office_equipment):

    def __init__(self, brand_name, price, inventory_number, unique_name):
        self.unique_name = unique_name
        Office_equipment.__init__(self, brand_name, price, inventory_number)

    def action(self):
        print(f'Принтер {self.brand_name} получен и он печатает')


class Scanner(Office_equipment):

    def __init__(self, brand_name, price, inventory_number, unique_name):
        self.unique_name = unique_name
        Office_equipment.__init__(self, brand_name, price, inventory_number)

    def action(self):
        print(f'Сканер {self.brand_name} получен и он сканирует')


class Xerox(Office_equipment):

    def __init__(self, brand_name, price, inventory_number, unique_name):
        self.unique_name = unique_name
        Office_equipment.__init__(self, brand_name, price, inventory_number)

    def action(self):
        print(f'Ксерокс {self.brand_name} получен и он копирует')


quantity = 0
item = {}

warehouse = Warehouse(quantity)

# Получаем оффисную технику на склад
list_tech = warehouse.receiving_warehouse(item)
print(list_tech)
# Выдаем оффисную технику на склад
# list_tech = [{'тип оргтехники': 'printer', 'производитель': 'hp', 'цену за ед': 25000,
#               'количество': 4, 'инветарный номер': '110/1'},
#              {'тип оргтехники': 'printer', 'производитель': 'canon', 'цену за ед': 23000,
#               'количество': 3, 'инветарный номер': '110/2'},
#              {'тип оргтехники': 'scanner', 'производитель': 'hp', 'цену за ед': 10000,
#               'количество': 4, 'инветарный номер': '120/1'},
#              {'тип оргтехники': 'scanner', 'производитель': 'canon', 'цену за ед': 12000,
#               'количество': 5, 'инветарный номер': '120/2'},
#              {'тип оргтехники': 'xerox', 'производитель': 'hp', 'цену за ед': 5000,
#               'количество': 3, 'инветарный номер': '130/1'},
#              {'тип оргтехники': 'xerox', 'производитель': 'canon', 'цену за ед': 6000,
#               'количество': 6, 'инветарный номер': '130/2'}]

un_name, br_name, pr, quant, inv_number = warehouse.transfer_to_department(list_tech)
print(f'Со склада выдан {un_name} марки {br_name} стоимостью {pr} руб., инвентарный номер {inv_number}')

if un_name == 'printer':
    printer = Printer(br_name, pr, inv_number, un_name)
    printer.action()
elif un_name == 'scanner':
    scanner = Scanner(br_name, pr, inv_number, un_name)
    scanner.action()
elif un_name == 'xerox':
    xerox = Xerox(br_name, pr, inv_number, un_name)

