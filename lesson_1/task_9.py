# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

print('Введите три разных числа')
first = int(input('первое: '))
second = int(input('второе: '))
third = int(input('третье: '))

if (second < first < third) or (third < first < second):
    print(first)
else:
    if (first < second < third) or (third < second < first):
        print(second)
    else:
        print(third)
