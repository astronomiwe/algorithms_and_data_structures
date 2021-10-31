# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.


# в задаче ряд чисел представляет собой последовательность рациональных дробей вида:
# -1/2 в степени (n-1), где n - номер элемента последовательности.


def sequence_sum_recursive(n: int):
    """Рекурсивная функция суммы элементов последовательности.
    n - количество элементов, sum - сумма элементов"""
    # базовый случай - n = 0 (не осталось элементов для суммирования)
    if n == 0:
        return 0
    else:
        current_elem = (-1/2)**(n-1)
        n -= 1
        return sequence_sum_recursive(n) + current_elem


quantity = int(input('введите натуральное число количества элементов последовательности: '))
print('result: ', sequence_sum_recursive(quantity))