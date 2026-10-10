import random

def is_valid(guess):
    if 1 <= guess <= 100:
        return True
    else:
        return False

def is_digit(guess):
    if guess.isdigit():
        return True
    else:
        return False

guessed_number = random.randint(1,100)

print(f'''==== Добро пожаловать в игру "Угадай число"! ====
Я загадал число от 1 до 100. Попробуйте его угадать!''')

guess = int(input("Введите ваше число: "))

while True:
    guess = int(input("Введите ваше число: "))
    if is_valid(guess):
        if guess < guessed_number:
            print("Ваше число меньше загаданного.")
        elif guess > guessed_number:
            print("Ваше число больше загаданного.")
        else:
            print("Вы угадали!")
            break
    else:
        print("Введено другое число! Введите число от 1 до 100.")

print("Спасибо за игру!")