
name = str(input("введите имя: "))
surname = str(input("Введите фамилию: "))
year_of_birth = str(input("Введите свой день рождения: "))
city = str(input("Введите свой город: "))
email = str(input("Введите свою почту: "))
phone = str(input("Введите свой телефон: "))


def my_func(*args):
    """
        :param name: Запрашиваем имя
        :param surname: Запрашиваем фамилию
        :param year_of_birth: Запрашиваем день рождения
        :param city: Запришиваем город проживания
        :param email: Запрашиваем почту
        :param phone: Запрашиваем телефон
        :return: Возвращаем значение
        Функция, принимает все вышеуказанные параметры, как именнованные аргументы.
        """
    print(f'ваши данные: {(args)}')

my_func(name,surname,year_of_birth,city,email,phone)

