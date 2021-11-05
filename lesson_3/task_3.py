# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

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
# получим индексы элементов, которые нужно поменять местами
for idx in range(1, len(array)):
    if array[idx] > max_el:
        max_el = array[idx]
        max_el_idx = idx
    elif array[idx] < min_el:
        min_el = array[idx]
        min_el_idx = idx

spam = array[max_el_idx]
array[max_el_idx] = array[min_el_idx]
array[min_el_idx] = spam

print(f'решение:         {array}')



