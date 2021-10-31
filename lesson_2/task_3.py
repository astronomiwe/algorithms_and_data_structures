# Сформировать из введенного числа
# обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


number = int(input('введите натуральное число: '))

to_flip = 0
copied_number = number  # сделаем копию числа, чтобы получить число разрядов исходного числа

while copied_number // 10 > 0:
    to_flip += 1
    copied_number = copied_number // 10  # оставляем от числа все разряды кроме младшего
    if copied_number // 10 == 0:  # если последний разряд, то выходим из цикла
        to_flip += 1
        break

flipped_number = 0

while to_flip > 0:
    if number < 10:
        digit = number

    else:
        if number < 100:
            digit = number % 10

        else:
            digit = number % (number // 10)  # получаем цифру, которую нужно перенести в младший разряд

    flipped_number += digit * 10 ** (to_flip - 1)

    number = number // 10

    to_flip -= 1

print(flipped_number)
