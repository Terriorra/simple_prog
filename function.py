###################################
# Импорт библиотек
###################################
import os
import sys

from random import randint
from random import choice
from random import sample


###################################
# Функция для загрузки и константы
###################################


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# Предложения поддержки при совершении ошибки в упражнении
path = resource_path('support')
with open(path, 'r', encoding='utf-8') as f:
    support = f.read().split('\n')

# Предложения похвалы при успешном решении упражнения
path = resource_path('susses')
with open(path, 'r', encoding='utf-8') as f:
    susses = f.read().split('\n')

# Кубок победителя
path = resource_path('cup')
with open(path, 'r', encoding='utf-8') as f:
    cup = f.read().split('\n')


class Quest:
    """
    Класс для хранения заданий
    """

    def __init__(self, text, ans):
        self.text = text
        self.ans = ans

    def __str__(self):
        return self.text


###################################
# Функции для генерации упражнений
###################################

# Тип 6
# Ниже приведена программа, записанная на пяти языках программирования.
#
# s = int(input())
# t = int(input())
# if s > 10 or t > 10:
#     print("YES")
# else:
#     print("NO")
#
# Было проведено 9 запусков программы, при которых в качестве значений переменных s и t вводились следующие пары чисел:
#
# (1, 2); (11, 2); (1, 12); (11, 12); (–11, –12); (–11, 12); (–12, 11); (10, 10); (10, 5).
#
# Сколько было запусков, при которых программа напечатала «YES»?


def create_expression():
    expression = ''

    sign = ['<', '>', '<=', '>=', '==']
    operator = ['and', 'or']
    match_operator = ['+', '-', '*', '/', '//', '%']
    not_operator = ['', 'not ']
    var = sample(['s', 't'], 2)

    match choice(range(1, 4)):
        case 1:
            # s < 5 or k < 5
            expression = (f'{choice(not_operator)}({var[0]} {choice(sign)} {randint(3, 15)}) '
                          f'{choice(operator)} {choice(not_operator)}({var[1]} {choice(sign)} {randint(3, 15)})')
        case 2:
            # s >= 2 * k
            expression = f'{var[0]} {choice(sign)} {randint(3, 15)} {choice(match_operator)} {var[1]}'
        case 3:
            # s // 2 == k
            expression = f'{var[0]} {choice(match_operator)} {randint(3, 15)} {choice(sign)} {var[1]}'

    return expression


def create_type_6():
    text = '''Ниже приведена программа, записанная на языке python
    
s = int(input())
t = int(input())
if expression:
    print("YES")
else:
    print("NO")
        
Было проведено n_col запусков программы, при которых в качестве значений переменных s и t вводились следующие пары 
чисел:
    
x_array.
    
Сколько было запусков, при которых программа напечатала «answer»?
     '''

    # Создам условия
    expression = create_expression()

    # Массив для хранения переменных
    x = []
    # Количество запусков программы
    n = randint(6, 12)
    # Что именно я считаю
    answer = choice(['YES', 'NO'])

    dict_ans = {0: 0, 1: 0}

    for _ in range(n):
        s = randint(1, 20)
        t = randint(1, 20)
        x.append((s, t))
        if eval(expression):
            dict_ans[0] += 1
        else:
            dict_ans[1] += 1

    text = text.replace('n_col', str(n))
    text = text.replace('x_array', '; '.join([str(i) for i in x]))
    text = text.replace('answer', answer)
    text = text.replace('expression', expression)

    ans = dict_ans[0] if answer == 'YES' else dict_ans[1]

    return Quest(text, ans)

# Тип 5.1
# У исполнителя Вычислитель две команды, которым присвоены номера:
#
# 1. умножь на 4
# 2. вычти b
#
# (b — неизвестное натуральное число)
#
# Первая из них увеличивает число на экране в 4 раза, вторая уменьшает его на b.
# Известно, что программа 12212 переводит число 3 в число 21.
#
# Определите значение b.


def create_command(a, b):
    actions = sample([('прибавь', '+'), ('раздели на', '/'), ('вычти', '-'), ('умножь на', '*')], 2)
    a, b = sample([a, b], 2)

    exp_1 = f'{actions[0][0]} {a}', f'{actions[0][1]} {a}'
    exp_2 = f'{actions[1][0]} b', f'{actions[1][1]} {b}'

    return exp_1, exp_2, b


def create_type_5_1():
    text = '''У исполнителя Вычислитель две команды, которым присвоены номера:

1. expression_1
2. expression_2

(b — неизвестное натуральное число)
Известно, что программа prog переводит число num_1 в число num_2.

Определите значение b.
    '''
    a = randint(2, 20)
    b = randint(2, 20)
    expressions = create_command(a, b)

    num_1 = randint(2, 20)
    num_2 = num_1
    prog = [str(choice('12')) for _ in range(randint(5, 10))]

    for i in prog:
        match i:
            case '1':
                num_2 = eval(f'{num_2} {expressions[0][1]}')
            case '2':
                num_2 = eval(f'{num_2} {expressions[1][1]}')

    text = text.replace('num_1', str(num_1))
    text = text.replace('num_2', str(round(num_2, 2)))
    text = text.replace('prog', ''.join(prog))
    text = text.replace('expression_1', expressions[0][0])
    text = text.replace('expression_2', expressions[1][0])

    return Quest(text, expressions[2])


# Тип 5.2
# У исполнителя Делитель две команды, которым присвоены номера:
#
# 1. раздели на 2
# 2. вычти 1
#
# Первая из них уменьшает число на экране в 2 раза, вторая уменьшает его на 1.
# Исполнитель работает только с натуральными числами. Составьте алгоритм получения из числа 65 числа 4,
# содержащий не более 5 команд. В ответе запишите только номера команд.

def create_type_5_2():
    text = '''У исполнителя Вычислитель две команды, которым присвоены номера:

    1. expression_1
    2. expression_2

    Составьте алгоритм получения из числа num_1 числа num_2, содержащий не более 5 команд.
        '''
    a = randint(2, 20)
    b = randint(2, 20)
    expressions = create_command(a, b)

    num_1 = randint(2, 20)
    num_2 = num_1
    prog = [str(choice('12')) for _ in range(randint(3, 5))]

    for i in prog:
        match i:
            case '1':
                num_2 = eval(f'{num_2} {expressions[0][1]}')
            case '2':
                num_2 = eval(f'{num_2} {expressions[1][1]}')

    text = text.replace('num_1', str(num_1))
    text = text.replace('num_2', str(round(num_2, 2)))
    text = text.replace('prog', ''.join(prog))
    text = text.replace('expression_1', expressions[0][0])
    text = text.replace('expression_2', expressions[1][0].replace('b', str(expressions[2])))

    return Quest(text, ''.join(prog))
