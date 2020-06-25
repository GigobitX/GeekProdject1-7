
ans1 = int(input("Введите 1 число: "))
ans2 = int(input("Введите 2 число: "))

def add(x,y):
    """
    :param x: Первый аргумент
    :param y: Второй аргумент
    :return: Возврат результата деления
    Функция делит первый аргумент на второй
    """
    if y == 0:
        y = int(input('Вы ввели нулевое значение, введите целое: '))
        result_int = x / y
        return result_int
    else:
        result_int = x/y
        return result_int


task_ans = int(add(ans1,ans2))

print(task_ans)