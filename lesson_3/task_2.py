# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# подготовка
from random import randint

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 50
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'\nисходный массив: {array}\n')

# первое решение
even_numbers_indexes = []
for idx in range(0, len(array)):
    if array[idx] % 2 == 0:
        even_numbers_indexes.append(idx)

print(f'первое решение: {even_numbers_indexes}\n')

# второе решение
second_even_numbers_indexes = [idx for idx in range(0, len(array)) if array[idx] % 2 == 0]
print(f'второе решение: {second_even_numbers_indexes} (с помощью list comprehension)')
