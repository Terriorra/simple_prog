from random import choice

from function import susses
from function import support
from function import cup
from function import create_var

n = 5  # количество правильных ответов

name = input('Как к тебе обращаться? ')
print(f'Приветствую, {name}.\nЗдесь 3 раздела. Для перехода на следующий раздел нужно ответить {n} раз правильно.')
input('Удачи.\nКогда будешь готов нажать enter...')

grade = 2

for var in range(1, 4):
    right = 0
    while right < n:
        q = create_var(var, n, right, grade)
        print(q.text)
        ans = input('Введи свой ответ: ').strip()
        if ans in q.ans:
            right += 1
            print(f'Правильно, {name}!')
            print(choice(susses))
        else:
            print(f'Не правильно, {name}!')
            print(choice(support))
            print(f'Правильный ответ: {choice(q.ans)}')

        input('Для продолжения нажми enter...')

    grade += 1
    print(f'Раздел {var} завершён, {name}!')
    print(choice(susses))
    print(f'Текущая оценка {grade}')
    input('Для продолжения нажми enter...')

print(f'Упражнение завершено, {name}')
print(choice(susses))
print()
print(cup)
input(' ')
input(' ')
input('Для завершения программы нажми enter...')
