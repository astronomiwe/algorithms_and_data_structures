# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# подготовка
from random import randint

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 50
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'\nисходный массив: {array}\n')

# решение

first = array[0]
first_idx = 0
second = None
second_idx = None

for idx in range(1, len(array)):
    if array[idx] < first:
        second = first
        second_idx = first_idx
        first = array[idx]
        first_idx = idx
    elif second == None or array[idx] < second:
        second = array[idx]
        second_idx = idx

print(f' {first = }      {first_idx = }')
print(f'{second = }    {second_idx = }')
