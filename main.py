import random
import time

def is_in_range(guess, start, end):
    if start <= guess <= end:
        return True
    else:
        return False

def correct_ending(num, word):
    endings = (('ок.', 'ку.', 'ки.'), ('.', 'у.', 'ы.'))

    if word == 'tryes':
        inner_tuple = 0
    elif word == 'seconds':
        inner_tuple = 1
 
    if num % 10 >= 5 or num % 10 == 0 or num // 10 % 10 == 1:
        ending = endings[inner_tuple][0]
    elif num % 10 == 1:
        ending = endings[inner_tuple][1]
    else:
        ending = endings[inner_tuple][2]
            
    return ending


print(f'''==== Добро пожаловать в игру "Угадай число"! ====
Я могу загадать число в любом диапазоне. 
Введите желаемый диапазон и попробуйте угадать число!
''')

start = int(input('Введите левую границу диапазона: '))
end = int(input('Введите правую границу диапазона: '))

if start == end:
    print(f'Я загадал число {start} и вы это прекрасно знаете! 🙂')

if start > end:
    print('Введены неверные границы диапазона. Не страшно, я поменял их местами.')
    start, end = end, start

guessed_number = random.randint(start, end)
count = 0

start_time = time.perf_counter()

while True:
    count += 1

    try:
        guess = int(input("Введите ваше число: "))
    except ValueError:
        print("Введено не целое число. Попробуйте еще раз.")
        continue

    if is_in_range(guess, start, end):
        if guess < guessed_number:
            print("Ваше число меньше загаданного.")
        elif guess > guessed_number:
            print("Ваше число больше загаданного.")
        else:
            print('====================================================')
            print(f'Вы угадали за {count} попыт{correct_ending(count, 'tryes')}')

            break

    else:
        print("Введено число вне диапазона! Введите число от {start} до {end}.")


end_time = time.perf_counter()
timing = end_time - start_time

print(f'Затраченное время: {round(timing)} секунд{correct_ending(timing, 'seconds')}')

if count <= 5:
    print(f'Ваша оценка: 💎 (бриллиант) Безупречная интуиция')
elif count <= 7:
    print(f'Ваша оценка: 🥇 (золото) Отличный результат! Идеальная стратегия бинарного поиска!')
elif count <= 10:
    print(f'Ваша оценка: 🥈 (серебро) Хороший результат!')
elif count <= 12:
    print(f'Ваша оценка: 🥉 (бронза) Умение есть, но можно лучше.')
else:
    print('Вам явно не везло, попробуйте стратегию \033]8;;https://habr.com/ru/articles/783848/\033\\бинарного поиска\033]8;;\033\\!')

print('Спасибо за игру!')