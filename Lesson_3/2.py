# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user_data(name_user, surname_user, year_birth_user, city_user, email_user, phone_number_user):
    return ', '.join([name_user, surname_user, year_birth_user, city_user, email_user, phone_number_user])


name = input('Имя: ')
surname = input('фамилия: ')
year_birth = input('год рождения: ')
city = input('город проживания: ')
email = input('email: ')
phone_number = input('телефон: ')

print(user_data(name, surname, year_birth, city, email, phone_number))
