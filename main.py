import random
import time
from math import log

def is_in_range(guess, start, end):
    if start <= guess <= end:
        return True
    else:
        return False


def correct_ending(num, word):
    endings = (('ок.', 'ку.', 'ки.'), ('.', 'а.', 'ы.'), ('ов.', 'о.', 'а.'))

    if word == 'tryes':
        inner_tuple = 0
    elif word == 'seconds':
        inner_tuple = 1
    elif word == 'points':
        inner_tuple = 2
 
    if num % 10 >= 5 or num % 10 == 0 or num // 10 % 10 == 1:
        ending = endings[inner_tuple][0]
    elif num % 10 == 1:
        ending = endings[inner_tuple][1]
    else:
        ending = endings[inner_tuple][2]
            
    return ending


def optimal_step_count(start, end):
    if start == end:
        return 1
    elif end - start == 1:
        return 2
    else:
        return int(log(end - start, 2)) + 1

def prises(grades):
    pepe = '''
____🐸🐸🐸🐸____🐸🐸🐸
___🐸🐸🐸🐸🐸__🐸🐸🐸🐸
__🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸
🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸
🐸🐸⚪️⚫️⚫️⚪️🐸🐸🐸⚪️⚫️⚫️⚪️
🐸⚪️⚫️⚫️⚪️⚫️⚪️🐸⚪️⚫️⚫️⚪️⚫️⚪️
🐸⚪️⚫️⚪️⚫️⚫️⚪️🐸⚪️⚫️⚪️⚫️⚫️⚪️
🐸🐸⚪️⚫️⚪️⚪️🐸🐸🐸⚪️⚫️⚪️⚪️
🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸
🔴🔴🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸
🐸🔴🔴🐸🐸🐸🐸🐸🐸🐸🐸🐸
🐸🐸🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
🐸🐸🐸🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴
🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸
🐸🐸🐸🐸🐸🐸🐸🐸🐸🐸
🐸🐸🐸🐸🐸🐸🐸🐸🐸'''

    giraffe = '''
_____________________________@@§³___§§§§§§
___________________________@@@____@@@
§§§§ss__________________@@@@@aa_@@@
§§§§§§§§§s_____▄▄▄____@@@@§§§§§§§@@
_§§§$$$$$§§§s__██▀▀▀▀▄▄@@§§§§§§§ §@@
__§§§$$$$$§§§§§██O°°°OOO██▄§§§§§§§§@@
___³§§§$$$$$§§§§█OoooOOOO█████▄█ ███▄▄_s§§§§§ss
_____³³§§§§§§§§§§█OOOOOOO█▀§§§§█O___OO▀█` 0o;▄$$
______________§§§█▄OOOO°█▀§@@▐█OooOOOOO▌
________________§§§█████▀§@@@@█OOOOOOO █
________________OO@@@@OOO@@@a█OOOOO█▀
_______________O@@OOOO@@▄OO§s@a█████▀
_______________@@O@@OO@@█OO³³@O§
_______________@@O@OOBB@@@§§@█@
_____________@@OOO@█▄BB@SWA§@§§§s
____________OOOO@@@██BBBB@³@§§§§
___________O@@OOOO@@█BBBBB@@§§
_________@O@O@OOOOOO██▄'''

    nyan_cat = '''
▒▒▒▒▒█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
▒▒▒▒▒█░▒▒▒▒▒▒▒▓▒▒▓▒▒▒▒▒▒▒░█
▒▒▒▒▒█░▒▒▓▒▒▒▒▒▒▒▒▒▄▄▒▓▒▒░█░▄▄
▄▀▀▄▄█░▒▒▒▒▒▒▓▒▒▒▒█░░▀▄▄▄▄▄▀░░█
█░░░░█░▒▒▒▒▒▒▒▒▒▒▒█░░░░░░░░░░░█
▒▀▀▄▄█░▒▒▒▒▓▒▒▒▓▒█░░░█▒░░░░█▒░░█
▒▒▒▒▒█░▒▓▒▒▒▒▓▒▒▒█░░░░░░░▀░░░░░█
▒▒▒▄▄█░▒▒▒▓▒▒▒▒▒▒▒█░░█▄▄█▄▄█░░█
▒▒▒█░░░█▄▄▄▄▄▄▄▄▄▄█░█▄▄▄▄▄▄▄▄▄█
▒▒▒█▄▄█░░█▄▄█░░░░░░█▄▄█░░█▄▄█'''

    seagulls = '''-----------------------
░░░░░░▄▀▀▀▄░░░░░░░░
▄███▀░◐░▄▀▀▀▄░░░░░░
░░▄███▀░◐░░░░▌░░░
░░░▌░▄▀▀▀▄░░░▌░░░░
▄███▀░◐░░░▌░░▌░░░░
░░░░▌░░░░░▐▄▄▌░░░░░
░░░░▌░░░░░▐▄▄░░░░░
░░░░▌░░░░▄▀▒▒▀▀▀▀▄
░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░▄▄▌▌▄▌▌░░░░░ '''

    doge = '''-----------------------
░░░░░░░█▐▓▓░████▄▄▄█▀▄▓▓▓▌█
░░░░░▄█▌▀▄▓▓▄▄▄▄▀▀▀▄▓▓▓▓▓▌█
░░░▄█▀▀▄▓█▓▓▓▓▓▓▓▓▓▓▓▓▀░▓▌█
░░█▀▄▓▓▓███▓▓▓███▓▓▓▄░░▄▓▐█
░█▌▓▓▓▀▀▓▓▓▓███▓▓▓▓▓▓▓▄▀▓▓▐█
▐█▐██▐░▄▓▓▓▓▓▀▄░▀▓▓▓▓▓▓▓▓▓▌█▌
█▌███▓▓▓▓▓▓▓▓▐░░▄▓▓███▓▓▓▄▀▐█
█▐█▓▀░░▀▓▓▓▓▓▓▓▓▓██████▓▓▓▓▐█
▌▓▄▌▀░▀░▐▀█▄▓▓██████████▓▓▓▌█▌
▌▓▓▓▄▄▀▀▓▓▓▀▓▓▓▓▓▓▓▓█▓█▓█▓▓▌█
█▐▓▓▓▓▓▓▄▄▄▓▓▓▓▓▓█▓█▓█▓█▓▓▓▐█ '''

    ass = '''
⠄⠄⣿⣿⣿⣿⠘⡿⢛⣿⣿⣿⣿⣿⣧⢻⣿⣿⠃⠸⣿⣿⣿⠄⠄⠄⠄⠄
⠄⠄⣿⣿⣿⣿⢀⠼⣛⣛⣭⢭⣟⣛⣛⣛⠿⠿⢆⡠⢿⣿⣿⠄⠄⠄⠄⠄
⠄⠄⠸⣿⣿⢣⢶⣟⣿⣖⣿⣷⣻⣮⡿⣽⣿⣻⣖⣶⣤⣭⡉⠄⠄⠄⠄⠄
⠄⠄⠄⢹⠣⣛⣣⣭⣭⣭⣁⡛⠻⢽⣿⣿⣿⣿⢻⣿⣿⣿⣽⡧⡄⠄⠄⠄
⠄⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣶⣌⡛⢿⣽⢘⣿⣷⣿⡻⠏⣛⣀⠄⠄
⠄⠄⠄⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙⡅⣿⠚⣡⣴⣿⣿⣿⡆⠄
⠄⠄⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠄⣱⣾⣿⣿⣿⣿⣿⣿⠄
⠄⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⠄
⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠣⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄
⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠑⣿⣮⣝⣛⠿⠿⣿⣿⣿⣿⠄
⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄ '''

    rep = '''
░░░░░░░░░░░░░██
░░░░░░░░░░░░█░░█
░░░░░░░░░░░░█░░█
░░░░░░░░░░░█░░░█
░░░░░░░░░░█░░░░█
████████▄▄█░░░░░███████████▄
▓▓▓▓▓▓▓█░░░░░░░░░░░░░░░░░░░█
▓▓▓▓▓▓▓█░░█░░░█▀█░█▀▀░█▀█░░░█
▓▓▓▓▓▓▓█▀▀█▀▀░█▀▄░█▀░░█▀▀░░░█
▓▓▓▓▓▓▓█░░█░░░▀░▀░▀▀▀░▀░░░░█
▓▓▓▓▓▓▓█░░░░░░░░░░░░░░░░░░█
▓▓▓▓▓▓▓█████░░░░░░░░░░░░░█
███████▀░░░░▀▀██████████▀ '''

    return 


def after_game_message(primal_grade, multiplier):
     
    grade_messages = (
        'Вам явно не везло, попробуйте стратегию \033]8;;https://habr.com/ru/articles/783848/\033\\бинарного поиска\033]8;;\033\\!',   
        'Ваша оценка: 🧠 (мегамозг) Да вы просто гений! Сломали систему!',
        'Ваша оценка: 🥉 (бронза) Умение есть, но можно лучше.',
        'Ваша оценка: 🥈 (серебро) Хороший результат!',
        'Ваша оценка: 🥇 (золото) Отличный результат! Идеальная стратегия бинарного поиска!',
        'Ваша оценка: 💎 (бриллиант) Безупречная интуиция'
    )

    grade = primal_grade * multiplier
    point_message = f'Получено {grade} очк{correct_ending(grade, 'points')}'

    print(f'{grade_messages[primal_grade]} \n{point_message}')

    return grade

def grading(current_steps, opt_steps):
    multiplier = opt_steps // 3 

    if current_steps <= opt_steps - int(opt_steps * 0.2) - 1:
        grade = after_game_message(5, multiplier)
        
    elif current_steps <= opt_steps:
        if opt_steps == 1:
            grade = after_game_message(1, multiplier)
        else:
            grade = after_game_message(4, multiplier)

    elif current_steps <= opt_steps + int(opt_steps * 0.2) + 1:
        grade = after_game_message(3, multiplier)
        
    elif current_steps <= opt_steps + int(opt_steps * 0.45) + 1:
        grade = after_game_message(2, multiplier)

    else:
        grade = after_game_message(0, multiplier)

    return grade


def main(game_count):
    if game_count == 0:
        print(f'      ==== Добро пожаловать в игру "Угадай число"! ====')
    else:
        print(f'      ==== Сыграем снова! ====')

    print(f'''Я могу загадать число в любом диапазоне. 
    Введите желаемый диапазон и попробуйте угадать число!
    От размера диапазона зависит количество начисляемых баллов.
    ''')

    start = int(input('Введите левую границу диапазона: '))
    end = int(input('Введите правую границу диапазона: '))

    if start == end:
        print(f'Думаю, вы прекрасно знаете, какое число я загадал!😏')

    if start > end:
        print('Введены неверные границы диапазона. Не страшно, я поменял их местами.')
        start, end = end, start

    print(f'''
                =======================
                Начинаем игру! 🎉
                =======================

    ''')

    guessed_number = random.randint(start, end)
    current_steps = 0
    start_time = time.perf_counter()

    while True:
        current_steps += 1

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
                print(f'Вы угадали за {current_steps} попыт{correct_ending(current_steps, 'tryes')}')
                break

        else:
            print(f"Введено число вне диапазона! Введите число от {start} до {end}.")

    end_time = time.perf_counter()
    timing = end_time - start_time
    opt_steps = optimal_step_count(start, end)

    print(f'Затраченное время: {round(timing)} секунд{correct_ending(timing, 'seconds')}')

    grade = grading(current_steps, opt_steps)

    return input('Хотите поиграть еще? (y/n): '), grade


grades = []
grades_sum = 0

while True:
    answer, grade = main(grades_sum)
    grades.append(grade)
    grades_sum += grade
 #   print(prises(grades))
    if answer.lower() != 'y':
        print(f'''
                ======================
                     До свидания!
                ======================
''')
        break
        