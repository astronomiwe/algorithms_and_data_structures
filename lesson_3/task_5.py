# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

# подготовка
from random import randint

SIZE = 5
MIN_ITEM = -10
MAX_ITEM = 10
array = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'\nисходный массив: {array}\n')

# решение

# сначала найдем минимальный элемент в массиве

# пусть минимальный и максимальный элемент массива - находится в ячейке 0
min = array[0]
min_idx = 0

# переберем остальной массив, сравним с min и max и
# получим индексы элементов, между которыми будем считать
for i in range(1, len(array)):
    if array[i] < min:
        min = array[i]
        min_idx = i

# найдем искомый элемент, который по условию задачи
# является числом в диапазоне [min, 0)

max_negative_num = min
max_negative_num_idx = min_idx

for j in range(0, len(array)):
    if 0 > array[j] >= max_negative_num:
        max_negative_num = array[j]
        max_negative_num_idx = j

print(f'{max_negative_num = }\n{max_negative_num_idx = }')
