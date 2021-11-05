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
max = array[0]
max_idx = 0

min = array[0]
min_idx = 0

# переберем остальной массив, сравним с min и max и
# получим индексы элементов, которые нужно поменять местами
for idx in range(1, len(array)):
    if array[idx] > max:
        max = array[idx]
        max_idx = idx
    elif array[idx] < min:
        min = array[idx]
        min_idx = idx

spam = array[max_idx]
array[max_idx] = array[min_idx]
array[min_idx] = spam

print(f'решение:         {array}')



