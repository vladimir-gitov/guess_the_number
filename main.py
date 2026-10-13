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
    else:
        print('Получено необработанное слово!')
        exit()

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


def all_prizes():
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

    seagulls = '''
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

    dolphin = '''
__________s§§§§ss.__.ss§§§§§§§§§ss.
____________?§§§§§§§§§§§§§§§§§§§§§§s.
_____________§§§§§§§§§§§§§§§§§§§§§§§?
_____________§§§§§§§§§§§§§§§§§§O§§§§§ s
____________s§§§§§§§§§§§§§§§§§§§§§s§§ §§§§s
___________s§§§§§§§§§§§§§§§§§§?§§§§§ ?????'
__________s§§§§§§§§§§§§§§???'
__________§§§§§§§§§§§§??'
_________s§§§§§§§§§??'
________s§§§§§§§§?
________§§§§§§?'
________§§§§§'
________§§§§'
________§§§'
________§§§
________§§§§ssss
______s§§§§§§§§§§§s,
_____s§§§§§§§???'
____§§§§???'''

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

    girl = ''' 
_______________________8888__8888888
_________________88888888888888888888888888
_______________8888ooo8888888888888888888888888
_____________8888oooooo8888888888888888888888888888
____________88oooooooo888ooo8888888888888888888888888
__________88888888oooo8ooooooooooo88888888888888888888
________888_8oo888888oooooooooooooooooo88888888888 888
___________88oooo88888888oooomoooooooooo88888888888 8
_________888888888888888888oMooooooooooo8888888888888
________88888888888888888888ooooooooooooM88888888888888
________8888888888888888888888oooooooooM8888888888888888
_________8888888888888888888888oooooooM888888888888888888
________8888888888888888oo88888ooooooM88888888888888888888
______88888888888888888ooo88888oooooM888888888888888 8888
_____88888888888888888ooo88888ooooMoo;o*M*o;888888888 88
____88888888888888888ooo8888oooooMooooooooooo88888888 8
___88888888888888888oooo88ooooooMo;ooooooooooo888888888
__8888888888888888888ooo8ooooooMooaAaooooooooM8888888888_______
__88___8888888888oo88oooo8ooooMooooooooooooo888888888888888_8888
_88__88888888888ooo8oooooooooMoooooooooo;oo88o88888888888888888
_8__8888888888888oooooooooooMoo"@@@@@"oooo8w8888888888888888
__88888888888o888ooooooooooMooooo"@a@"oooooM8i888888888888888
_8888888888oooo88oooooooooM88oooooooooooooM88z88888888888888888
8888888888ooooo8oooooooooM88888oooooooooMM888!888888888888888888
888888888ooooo8oooooooooM8888888MAmmmAMVMM888*88888888___88888888
888888_MoooooooooooooooM888888888oooooooMM88888888888888___8888888
8888___MooooooooooooooM88888888888ooooooMM888888888888888____88888
_888___MoooooooooooooM8888888888888MooooomM888888888888888____8888
__888__MooooooooooooM8888o888888888888oooomooMm88888_888888___8888
___88__Moooooooooooo8888o88888888888888888ooooooMm8___88888___888
___88__Moooooooooo8888Moo88888oo888888888888oooooooMm88888____88
___8___MMoooooooo8888Mooo8888ooooo888888888888ooooooooMm8_____8
_______8Mooooooo8888Mooooo888ooooooo88ooo8888888ooooooooMm____8
______88MMooooo8888Mooooooo88oooooooo8ooooo888888oooMoooooM
_____8888Mooooo888MMoooooooo8oooooooooooMoooo8888ooooMooooM
____88888Mooooo88oMoooooooooo8oooooooooooMooo8888ooooooMooM
___88_888MMooo888oMoooooooooooooooooooooooMo8888oooooooooMo
___8_88888Mooo88ooMoooooooooooooooooooooooMMo88ooooooooooooM
_____88888Mooo88ooMoooooooooo*88*ooooooooooMo88ooooooooooooooM
____888888Mooo88ooMooooooooo88@@88ooooooooMoo88ooooooooooooooM
____888888MMoo88ooMMoooooooo88@@88oooooooMooo8ooooooooooooooo*8
____88888__Mooo8ooMMooooooooo*88*ooooooooooMooooooooooooooooo88@@
____8888___MMooooooMMoooooooooooooooooooooMMooooooooooooooooo88@@
_____888____MoooooooMMoooooooooooooooooooMMooMooooooooooooooooo*8
_____888____MMoooooooMMMooooooooooooooooMMoooMMoooooooooooooooM
______88_____MooooooooMMMMoooooooooooMMMMoooooMMooooooooooooMM
_______88____MMoooooooooMMMMMMMMMMMMMooooooooMMMooooooooMM
________88____MMooooooooooooMMMMMMMooooooooooooMMMMMMMMMM
_________88___8MMooooooooooooooooooooooooooooooooooMMMMMM
__________8___88MMooooooooooooooooooooooMoooMooooooooMM
______________888MMooooooooooooooooooMMooooooMMooooooMM
_____________88888MMoooooooooooooooMMMooooooomMoooooMM
_____________888888MMoooooooooooooMMMoooooooooMMMoooM
____________88888888MMoooooooooooMMMoooooooooooMMoooM
___________88_8888888MoooooooooMMMooooooooooooooMoooM
___________8__888888_MoooooooMMoooooooooooooooooMoooMo
______________888888_MooooooMoooooooooooooooooooMoooMM
_____________888888__MoooooMooooooooooooooooooooooooMoM
_____________888888__MoooooMooooooooo@ooooooooooooooMooM
_____________88888___Moooooooooooooo@@oooooooooooooooMooM
____________88888___Moooooooooooooo@@@ooooooooooooooooMooM
___________88888___Mooooooooooooooo@@ooooooooooooooooooMooM
__________88888___Mooooomoooooooooo@ooooooooooMmoooooooMoooM
__________8888___MoooooMoooooooooooooooooooooooMMoooooooMoooM
_________8888___MoooooMoooooooooooooooooooooooMMMooooooooMoooM
________888____MoooooMmooooooooooooooooooooooMMMoooooooooMooooM
______8888____MMooooMmoooooooooooooooooooooMMMMooooooooomoomoooM
_____888______MoooooMooooooooooooooooooooMMMooooooooooooMoommoooM
__8888_______MMoooooooooooooooooooooooooMMooooooooooooomMooMMoooMo
_____________MoooooooooooooooooooooooooMooooooooooooooomMooMMoooMm
____________MMoooooomoooooooooooooooooooooooooooooooooooMooMMoooMM
____________MooooooooMoooooooooooooooooooooooooooooooooooMooMoooMM
___________MMoooooooooMoooooooooooooMoooooooooooooooooooooMoMoooMM
___________MoooooooooooM8ooooooooooMoooooooooooooooooooooooMMooMMM
___________Moooooooooooo88ooooooooMooooooooooooooooooooooooMMooMM
___________Mooooooooooooo88ooooooMoooooooooooooooooooooooooMooMM
___________Moooooooooooooo88oo0oMoooooooooooooooooooooooooMooMM
___________Mooooooooooooooo88o8oMoooooooooooooooooooooooooMoMM
___________Mooooooooooooooooo88MooooooooooooooooooooooooooMMM
___________MoooooooooooooooooooMooooooooooooooooooooooooooMMM
___________MMoooooooooooooooooMooooooooooooooooooooooooooMMM
____________MoooooooooooooooooMooooooooooooooooooooooooooMMM
____________MMoooooooooooooooMooooooooooooooooooooooooooMMM
_____________MoooooooooooooooMoooooooooooooooooooooooooMMM
_____________MMoooooooooooooMoooooooooooooooooooooooooMMM
______________MoooooooooooooMooooooooooooooooooooooooMMM
______________MMoooooooooooMooooooooooooooooooooooooMMM
_______________MoooooooooooMoooooooooooooooooooooooMMM
_______________MMoooooooooMoooooooooooooooooooooooMMM
________________MoooooooooMooooooooooooooooooooooMMM
________________MMoooooooMooooooooooooooooooooooMMM
_________________MMooooooMoooooooooooooooooooooMMM
_________________MMoooooMoooooooooooooooooooooMMM
__________________MMooooMooooooooooooooooooooMMM
__________________MMoooMooooooooooooooooooooMMM
___________________MMooMoooooooooooooooooooMMM
___________________MMoMoooooooooooooooooooMMM
____________________MMMooooooooooooooooooMMM
____________________MMooooooooooooooooooMMM
_____________________MoooooooooooooooooMMM
____________________MMooooooooooooooooMMM
____________________MMoooooooooooooooMMM
____________________MMooooMoooooooooMMMo
____________________mMMooooMMoooooooMMMM
_____________________MMMoooooooooooMMMoM
_____________________mMMoooMoooooooMoMoM
______________________MMooMMMMoooooooMoM
______________________MMooMMMooooooooMoM
______________________mMMooMMooooooooMoM
_______________________MMooMMoooooooooMoM
_______________________MMooMMooooooooooMom
_______________________MMoooMoooooooooooMM
_______________________MMMoooooooooooooooMo
_______________________MMMoooooooooooooooMo
_______________________MMMooooooooooooooooM
_______________________MMMooooooooooooooooM
_______________________MMMooooooooooooooooMm
________________________MMooooooooooooooooMM
________________________MMMoooooooooooooooMM
________________________MMMoooooooooooooooMM
________________________MMMoooooooooooooooMM
________________________MMMoooooooooooooooMM
_________________________MMooooooooooooooMMM
_________________________MMMoooooooooooooMM
_________________________MMMoooooooooooooMM
_________________________MMMooooooooooooMM
__________________________MMooooooooooooMM
__________________________MMooooooooooooMM
__________________________MMoooooooooooMM
__________________________MMMooooooooooMM
__________________________MMMooooooooooMM
___________________________MMoooooooooMM
___________________________MMMooooooooMM
___________________________MMMooooooooMM
____________________________MMooooooooMM
____________________________MMMooooooMM
____________________________MMMooooooMM
_____________________________MMooooooMM
_____________________________MMooooooMM
______________________________MMoooooMM
______________________________MMoooooMMo
______________________________MMoooooMoM
______________________________MMoooooMoM
______________________________oMooooooMo
_____________________________MoMoooooooM
____________________________MoooMooooooM
___________________________MooooMooooooM
__________________________MoooooMoooooooM
_________________________MooooooMMoooooooM
_________________________MoooooooMooooooooM '''

    prizes = (('rep', float('inf'), rep), 
              ('Чайки', 5, seagulls), 
              ('Дельфин', 10, dolphin), 
              ('Жираф', 15, giraffe), 
              ('Нян кэт', 20, nyan_cat), 
              ('Пепе', 25, pepe), 
              ('Попа', 50, ass), 
              ('Девушка', 150, girl))

    return prizes
    

def after_game_message(primal_grade, multiplier):
     
    grade_messages = (
        'Вам явно не везло, попробуйте стратегию \033]8;;https://habr.com/ru/articles/783848/\033\\бинарного поиска\033]8;;\033\\!',   
        'Ваша оценка: 🧠 (мегамозг) Да вы просто гений! Сломали систему! Но это не точно.',
        'Ваша оценка: 🥉 (бронза) Умение есть, но можно лучше.',
        'Ваша оценка: 🥈 (серебро) Хороший результат!',
        'Ваша оценка: 🥇 (золото) Отличный результат! Идеальная стратегия бинарного поиска!',
        'Ваша оценка: 💎 (бриллиант) Безупречная интуиция'
    )

    grade = primal_grade * multiplier
    point_message = f'Получено {grade} очк{correct_ending(grade, "points")}'

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
    elif game_count == 5:
        print(all_prizes()[0][2])
        print('Ваша пятая игра!')
    else:
        print(f'''
      ==== Сыграем снова! ====''')

    print(f'''    Я могу загадать число в любом диапазоне. 
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
            guess = int(input('Введите ваше число: '))
        except ValueError:
            print('Введено не целое число. Попробуйте еще раз.')
            continue

        if is_in_range(guess, start, end):
            if guess < guessed_number:
                print('''Ваше число меньше загаданного.
                ''')
            elif guess > guessed_number:
                print('''Ваше число больше загаданного.
                ''')
            else:
                print('====================================================')
                print(f'Вы угадали за {current_steps} попыт{correct_ending(current_steps, "tryes")}')
                break

        else:
            print(f"Введено число вне диапазона! Введите число от {start} до {end}.")

    end_time = time.perf_counter()
    timing = int(end_time - start_time)
    opt_steps = optimal_step_count(start, end)

    print(f'Затраченное время: {round(timing)} секунд{correct_ending(timing, "seconds")}')

    grade = grading(current_steps, opt_steps)

    return grade


grades_sum = 0
game_count = 0
prizes = all_prizes()

while True:
    grade = main(game_count)
    game_count += 1
    grades_sum += grade
    get_prize = input(f'''У вас {grades_sum} очк{correct_ending(grades_sum, "points")} 
Хотите посмотреть призы? (y/n): ''') 

    if get_prize.lower() == 'y':

        while True:
            print('''Выберите приз! 
Чтобы выбрать, введите соответствующее число
0 — выйти из меню''')
            for i in range(1, len(prizes)):
                print(f'{i} — {prizes[i][0]}! Стоит {prizes[i][1]} очк{correct_ending(prizes[i][1], "points")}')
            
            try:
                choice = int(input())
            except ValueError:
                continue
            
            if choice == 0:
                break
            elif int(choice) in range(1, len(prizes)):
                if grades_sum >= prizes[choice][1]:
                    print(f'{prizes[choice][2]} \nВы выиграли приз!')
                    grades_sum -= prizes[choice][1]
                    print(f'Осталось очков: {grades_sum}')
                    if input('Вернуться в комнату призов? (y/n)') != 'y':
                        break
                else:
                    print('У вас недостаточно очков!')
                    if input('Хотите вернуться в призовую комнату? (y/n):') != 'y':
                        break


    answer = input('Хотите поиграть еще? (y/n)')
    if answer.lower() != 'y':
        print(f'''
                ======================
                   Спасибо за игру!
                     До свидания!
                ======================
''')
        break