import os
import sys


def wage_func(*args):
    """
    :param args: принимет аргументы из формулы (выработка в часах * ставка в час) + премия
    :return: возверащает эти значения
    """
    return (jw * rh) + award

jw = int(input("Укажите выработку в часах: "))
rh = int(input("Укажите ставку в час: "))
award = int(input("Укажите премию: "))

print(wage_func())
