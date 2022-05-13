"""Создайте функцию filter_even, которая принимает на вход список целых чисел,
и фильтруя, возвращает список, содержащий только четные числа.
Используйте filter для фильтрации и lambda."""

def filter_even(li):
    list_second = list(filter(lambda x: x % 2 == 0, li)) #список с фильтром на четность
    return list_second

list_first = list(map(int, input("введите ряд чисел: ").split())) 

print(filter_even(list_first))