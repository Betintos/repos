'==========Функция высшего порядка=========='
# это функция, которая принимает в аргументы другую функцию,
# создает другую функцию
# обрабатывает функцию и возврашает функцию

# функция, принимающая в качестве аргументов другие функции
# и/или возвращающая другую функцию в качестве результата

# def func1():
#     return 'hi'

# def func2(func_):
#     print(func_())

# func2(func1)

'==========Декораторы=========='
# это функции высшего порядка, которые нужны для расширения
# функционала другой функции, не изменяя ее (функция оберток)

# def decorator_silencer(func):
#     def wrapper(*args, **kwargs):
#         text = func()
#         res = 'тихо ' + text
#         print(res)
#     return wrapper

# def gun():
#     return 'стрелять'

# wrapper = decorator_silencer(gun) # способ использования декоратора вручную 
# wrapper()

# def decorator_silencer(func):
#     def wrapper(*args, **kwargs):
#         text = func()
#         res = 'тихо ' + text
#         print(res)
#     return wrapper

# @decorator_silencer # синтаксический сахар
# def gun():
#     return 'стрелять'

# gun()

'-------------------------------------------'

from datetime import datetime

# def decorator(func):
#     def wrapper():
#         print('start: ', datetime.now())
#         func()
#         print('finish', datetime.now())
#     return wrapper

# def hello():
#     print('hello')

# wrapper = decorator(hello)
# wrapper()

'---------------------------------------------'

# def funct_start_time(func):
#     def wrapper(*args, **kwargs):
#         print('start: ', datetime.now())
#         func(*args, **kwargs)
#     return wrapper

# def sum_(a, b):
#     print(a + b)

# wrapper = funct_start_time(sum_)
# wrapper(10, 20)

'-----------------------------------------------'

def decorator(num):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return inner_decorator

@decorator(10)
def hello():
    print('hello world')

hello()