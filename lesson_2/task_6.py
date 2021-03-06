# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

from random import randint

print('игра "отгадайте число от 0 до 100. у Вас 10 попыток."')

count = 0
secret = randint(0, 100)

# блок отгадывания, не пускает на 11 попытку
while True:
    count += 1
    answer = int(input(f'Попытка номер {count}. Введи число от 0 до 100: '))

    if answer == secret:
        print('Вы угадали загаданное число')
        break
    else:
        if count == 10:
            print(f'Вы не справились за 10 попыток, загаданное число: {secret}')
            break
        else:
            if answer < secret:
                print('Ваше число меньше загаданного')
            else:
                print('Ваше число больше загаданного')
