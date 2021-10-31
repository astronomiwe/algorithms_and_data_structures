# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_number = int(input("введите трёхзначное число"))

# находим цифру каждого разряда
digit_3 = user_number % 10
digit_2 = user_number % 100 // 10
digit_1 = user_number // 100


# блок нахождения суммы цифр
digit_sum = digit_1 + digit_2 + digit_3
print("сумма цифр числа:", digit_sum)

# блок нахождения произведения цифр
digit_multiply = digit_1 * digit_2 * digit_3
print("произведение цифр числа:", digit_multiply)


