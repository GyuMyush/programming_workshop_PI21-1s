"""Напишите функцию бинарного поиска bin_search,
которая принимает на вход отсортированный списоки элемент.
Функция должна возвращать индекс искомого элемента в списке."""

li = list(map(int, input("введите ряд чисел: ").split()))
elemen = int(input("Введите искомый элемент: "))

def bin_search(li, element):
    li.sort()

    low = 0
    high = len(li) - 1
    mid = (low + high) // 2

    while element != li[mid]:
        if element > li[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2

    return(mid)


print(bin_search(li, elemen))