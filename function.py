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
    not_oper = ['', 'not ']
    var = sample(['s', 't'], 2)

    match choice(range(1, 4)):
        case 1:
            # s < 5 or k < 5
            expression = (f'{choice(not_oper)}({var[0]} {choice(sign)} {randint(3, 15)}) '
                          f'{choice(operator)} {choice(not_oper)}({var[1]} {choice(sign)} {randint(3, 15)})')
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

#
# a = create_type_6()
# print(a)
# print(a.ans)
