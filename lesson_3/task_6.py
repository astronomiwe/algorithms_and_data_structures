# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# подготовка
from random import randint

SIZE = 15
MIN_ITEM = -20
MAX_ITEM = 20
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'\nисходный массив: {array}\n')

# решение

# пусть минимальный и максимальный элемент массива - находится в ячейке 0
max_el = array[0]
max_el_idx = 0

min_el = array[0]
min_el_idx = 0

# переберем остальной массив, сравним с min_el и max_el и
# получим индексы элементов, между которыми будем считать
for idx in range(1, len(array)):
    if array[idx] > max_el:
        max_el = array[idx]
        max_el_idx = idx
    elif array[idx] < min_el:
        min_el = array[idx]
        min_el_idx = idx

# нужно понять, как расположены макс. и мин. элементы относительно друг друга (кто левее, кто правее), чтобы
# корректно проитерироваться по массиву и вычислить сумму
print(f'{min_el = }  {min_el_idx = }\n{max_el = }  {max_el_idx = }\n')

# зададим сумму элементов = 0
sum_between = 0


def sum_between(first_idx, second_idx, array):
    """функция возвращает сумму элементов переданного массива arr
    между двумя элементами с индексами first_idx и second_idx"""
    total = 0
    if first_idx < second_idx:
        for idx in range(first_idx + 1, second_idx):
            total += array[idx]
    elif second_idx < first_idx:
        for idx in range(second_idx + 1, first_idx):
            total += array[idx]
    return total


print(f'сумма элементов между: {sum_between(min_el_idx, max_el_idx, array)}')
