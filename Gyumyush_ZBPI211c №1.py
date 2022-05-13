"""1. Напишите рекурсивную функцию fact,
которая вычисляет факториал заданного числа x."""

def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)

num = int(input("введите число: "))
print (f'Факториал числа {num} - это {fact(num)}')