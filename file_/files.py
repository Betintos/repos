'========== Modules & packages =========='
# .py - module 
# group of modules - package

'========== Files =========='
# open() - функция, которая открывает файл в определенном режиме

# Режимы:
# 1. r - read (только для чтения)
# 2. w - wite (только для записи, каждый раз файл очищается)
# 3. a - append (только для дозаписи, добавляется в конец)
# 4. x - создает файл, но если файл уже существует - выйдет ошибка

'========== Read =========='

# file = open('test1.txt', 'r')
# print(file.read())
# file.seek(0) # возвращает курсов на указанный индекс
# print(file.read())
# print(file.read(2))
# print(file.readline()) -> str
# print(file.readline())
# print(file.readlines()) -> list[str]
# print(file.tell())
# file.close()

'========== Write =========='

# file = open('test2.txt', 'w')
# file.write('Makers\nMake the World\n')
# file.writelines(['Hello World\n', 'Makers\n'])
# file.close()

# write(str), writelines(list[str])

'========== Append =========='

# file = open('test1.txt', 'a')
# file.write('py33\n')
# file.write('append\n')
# file.close()

'========== Контекстный менеджер =========='

# with

with open('test1.txt') as f:
    print(f.read()) # конструкция with сама закрывает файл

print(f.closed) # True