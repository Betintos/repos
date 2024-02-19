'=======Области видимости======='
# LEGB - Local Enclosed Global Build-in

'===Build-in==='
# встроенное пространство имен
# (list, print, len, input)

'===Global==='
# все переменные которые мы создали сами
# функция globals для просмотра всех глобальных переменных

# a = 10
# b = 'hello'
# print(globals())

'===Enclosed==='
# замкнутое пространство имен - это локальное пространство,
# у которого есть внутреннее пространство

# var = 'global' # хранится в глобальном пространстве
# def func():
#     var = 'enclosed'
#     def inner_func():
#         var = 'local'
#         print(var)
#     print(var)
#     inner_func()
# print(var)
# func()

'===Local==='
# локальное пространство имен - это пространство,
# которое находится внутри функции

# a = 10
# def func(a, b):
#     res = a + b
#     print(res)
#     print(locals())
#     print(globals())
# func(10 ,5)

# to access variables in enclosed space from local space -
# use keyword 'nonlocal'