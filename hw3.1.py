def add(x,y):
    """
    :param x: Первый аргумент
    :param y: Второй аргумент
    :return: Возврат результата деления
    Функция делит первый аргумент на второй
    """
    x = int(input("Введите 1 число: "))
    y = int(input("Введите 2 число: "))
    if y == 0:
        y = int(input('Вы ввели нулевое значение, введите целое: '))
        result_int = x / y
        return result_int
    else:
        result_int = x/y
        return result_int


task_ans = add(3,5)

print("решение будет равно: " + task_ans)