'===============Встроенные функции================='
# map, filter, reduce, zip

'ZIP'
# соединяет несколько последовательностей (получаем 
# генератор, в котром элементы - tuple)  (zip object)
# ex: <zip object at 0x103090a80>

# list_1 = [1, 2, 3, 4]
# list_2 = ['a', 'b', 'c']
# list_3 = [10.5, 20.0, 1.3, 0.5]

# zipped = zip(list_1, list_2)
# print(zipped)
# print(list(zipped))
# print(tuple(zipped))
# print(dict(zipped)) # работает только с 2 списками в zip()

'ENUMERATE'
# нумерует последовательность (по усмолчанию с 0),
# (также возвращает генератор)
# ex: <enumerate object at 0x102a1f7e0>

# enumerated = enumerate('hello world')
# print(enumerated)
# print(list(enumerated))

# for elem in enumerated:
#     print(elem)

'MAP'
# принимаает функцию и последовательность
# записывает в новую последовательность рузультат применения 
# функции на заданную последовательность
# (возвращает генератор)
# ex: <map object at 0x1025edb70>

# list_ = ['1', '2', '3', '4']
# mapped = map(int, list_) 
# print(mapped)
# print(list(mapped))

# list_ = ['1awd', '245', '3sss', '43']
# mapped = map(str.isdigit, list_)
# print(list(mapped))

# def myFunc(x):
#     return x ** 2
# nums = [1, 76, 33, 10]
# print(list(map(myFunc, nums)))
# print(list(map(lambda x: x**2, nums)))

# str_ = 'hello world'
# mapped = map(str.upper, str_)
# print(''.join(list(mapped)))

'FILTER'

# возвращает генератор с элементами, прошедшими фильтрацию (условие),
# принимает функцию и последовательность

list_ = [12, -23, 0, -4, 5, -89]
filtered = filter(lambda x: x >= 0, list_)
print(list(filtered))

# users = [
#     {'name': 'makers', 'age': 20},
#     {'name': 'anonym', 'age': 15},
#     {'name': 'sam', 'age': 25}
# ]

# adults = filter(lambda user: user['age'] >= 18, users)
# print(list(adult))

# adults = filter(lambda user: user['name'].startswith('a'), users)
# print(list(adults))

'REDUCE'

# принимает функцию и последовательность, вовращает один элемент 
# (передаваемая функция должна принимать два аргумента)
# импортируется из functools

# from functools import reduce

# list_ = [1, 45, 6, 43, 657]
# res = reduce(lambda x, y: x * y, list_)
# print(res)

# users = [
#     {'name': 'makers', 'age': 20},
#     {'name': 'anonym', 'age': 15},
#     {'name': 'sam', 'age': 25}
# ]
# def youngest(user1, user2):
#     if user1['age'] < user2['age']:
#         return user1
#     else:
#         return user2

# print(reduce(youngest, users))

# list_ = [1, 2, 4, 6, 1, 9, -1, 6, -12]

# print(reduce(lambda num1, num2: num1 if num1 < num2 else num2, list_))