# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)


# блок ввода чисел
print('Введите три разных числа')
first = int(input('первое: '))
second = int(input('второе: '))
third = int(input('третье: '))

# блок сравнения и вывода
if (second < first < third) or (third < first < second):
    print(first)
else:
    if (first < second < third) or (third < second < first):
        print(second)
    else:
        print(third)
