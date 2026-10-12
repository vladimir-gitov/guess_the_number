import random

def is_in_range(guess):
    if 1 <= int(guess) <= 100:
        return True
    else:
        return False


guessed_number = random.randint(1,100)
count = 0


print(f'''==== Добро пожаловать в игру "Угадай число"! ====
Я загадал целое число от 1 до 100. Попробуйте его угадать!''')

while True:

    count += 1

    try:
        guess = int(input("Введите ваше число: "))
    except ValueError:
        print("Введено не целое число. Попробуйте еще раз.")
        continue

    if is_in_range(guess):
        if guess < guessed_number:
            print("Ваше число меньше загаданного.")
        elif guess > guessed_number:
            print("Ваше число больше загаданного.")
        else:
            print(f'Вы угадали за {count} попыток.')
            break
    else:
        print("Введено число вне диапазона! Введите число от 1 до 100.")

if count <= 5:
    print(f'Ваша оценка: 💎 (бриллиант) Безупречная интуиция')
elif count <= 7:
    print(f'Ваша оценка: 🥇 (золото) Отличный результат! Идеальная стратегия бинарного поиска!')
elif count <= 10:
    print(f'Ваша оценка: 🥈 (серебро) Хороший результат!')
elif count <= 12:
    print(f'Ваша оценка: 🥉 (бронза) Умение есть, но можно лучше.')
else:
    print("Вам явно не везло, попробуйте \033]8;;https://habr.com/ru/articles/783848/\033\\бинарный поиск\033]8;;\033\\!")

print('Спасибо за игру!')