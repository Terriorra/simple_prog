###################################
# Импорт библиотек
###################################
import os
import sys

from random import randint
from random import choice
from random import sample

from itertools import product


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
    cup = f.read()

# Описание задания и решение
path = resource_path('about')
with open(path, 'r', encoding='utf-8') as f:
    about = f.read().split('\n\n\n')


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
# Функции для вывода текста
###################################


sign_hor = '═'
sign_vert = '║'
LINE_LEN = 70


def print_text(text, len_string):
    s = [f" {(len_string - 2) * sign_hor} "]

    for line in text:
        if len(line) + 4 < len_string:
            s.append(f"{sign_vert} {line}{(len_string - len(line) - 4) * ' '} {sign_vert}")
        else:
            s += cut_string(line, len_string)
    s.append(f" {(len_string - 2) * sign_hor} ")

    return s


def cut_string(text, len_string):
    s = []

    text = text.split(' ')
    lines = []
    now = ''
    for i in text:
        if len(now + ' ' + i) < len_string - 4:
            now += ' ' + i
        else:
            lines.append(now)
            now = i
    lines.append(now)

    for line in lines:
        s.append(f"{sign_vert} {line}{(len_string - 4 - len(line)) * ' '} {sign_vert}")

    return s


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

    return Quest(text, [str(ans)])


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

    return Quest(text, [str(expressions[2])])


# Тип 5.2
# У исполнителя Делитель две команды, которым присвоены номера:
#
# 1. раздели на 2
# 2. вычти 1
#
# Первая из них уменьшает число на экране в 2 раза, вторая уменьшает его на 1.
# Исполнитель работает только с натуральными числами. Составьте алгоритм получения из числа 65 числа 4,
# содержащий не более 5 команд. В ответе запишите только номера команд.

# Создам список из все возможных и подходящих команд
prog_all = []
for n_now in range(2, 6):
    for i_now in product('12', repeat=n_now):
        s_now = ''.join(i_now)
        if len(set(s_now)) > 1:
            prog_all.append(s_now)


def prog_count(x, prog, expressions):
    for i in prog:
        match i:
            case '1':
                x = eval(f'{x} {expressions[0][1]}')
            case '2':
                x = eval(f'{x} {expressions[1][1]}')
    return str(round(x, 2))


def create_type_5_2():
    text = '''У исполнителя Вычислитель две команды, которым присвоены номера:

    1. expression_1
    2. expression_2

    Составьте алгоритм получения из числа num_1 числа num_2, содержащий не более 5 команд.
        '''
    # Константа для первой команды
    a = randint(2, 20)
    # Константа для второй команды
    b = randint(2, 20)
    # Создадим две команды
    expressions = create_command(a, b)

    # Старт
    num_1 = randint(2, 20)

    # Выберем набор команд
    prog = choice(prog_all)

    num_2 = prog_count(num_1, prog, expressions)

    ans = [prog]

    for i in prog_all:
        if prog_count(num_1, i, expressions) == num_2:
            ans.append(i)

    ans = list(set(ans))

    text = text.replace('num_1', str(num_1))
    text = text.replace('num_2', num_2)
    text = text.replace('prog', ''.join(prog))
    text = text.replace('expression_1', expressions[0][0])
    text = text.replace('expression_2', expressions[1][0].replace('b', str(expressions[2])))

    return Quest(text, ans)


###################################
# Генерация вопроса
###################################

def create_var(var, n, right, grade):
    os.system("CLS")

    text = f'''Текущий раздел: {var} из 3
Осталось решить: {n - right} из {n}
Текущая оценка: {grade}'''

    text = print_text(text.split('\n'), LINE_LEN)

    text += print_text(about[0].split('\n'), LINE_LEN)

    ans = ''
    q = Quest(text, ans)

    match var:
        case 1:
            text += print_text(about[1].split('\n'), LINE_LEN)
            q = create_type_6()
        case 2:
            text += print_text(about[2].split('\n'), LINE_LEN)
            q = create_type_5_1()
            while str(q.ans) == '0.0':
                q = create_type_5_1()
        case 3:
            text += print_text(about[3].split('\n'), LINE_LEN)
            q = create_type_5_2()

    text += print_text(q.text.split('\n'), LINE_LEN)

    q.text = '\n'.join(text)

    return q
