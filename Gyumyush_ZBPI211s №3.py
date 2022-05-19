"""Напишите функцию square ,которая принимает на вход список целых чисел
и возвращает список с возведенными в квадрат элементами.Используйте map."""

def squere(list_int):
    list_int = list(map(int, list_int))
    list_int = [i ** 2 for i in list_int]
    return(list_int)

list_int = input("введите ряд чисел: ").split()

print(squere(list_int))