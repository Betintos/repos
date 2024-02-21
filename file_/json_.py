'========== JSON =========='

# JavaScript Object Notation - универсальный формат, в котором мы можем
# хранить данные в типах данных понятных почти для всех языков программирования

import json
 
# десериализация - перевод с json строки в в python объекты
# loads - метод для десериализации с json строки
# load - метод для десериализации с json файла

# json_list = '[1, 2, 3, 4, 5]'
# python_list = json.loads(json_list)
# print(python_list)

# json_data = 'true'
# python_data = json.loads(json_data)
# print(python_data)

# json_data = 'null'
# python_data = json.loads(json_data)
# print(python_data)

# with open('test.json', 'r') as file:
#     python_data = json.load(file)
# print(python_data)

# сериализация - переаод python объектов в json строку
# dumps - метод для сериализации в json строку
# dump - метод для сериализации в json файл

python_data = None
json_data = json.dumps(python_data)
print(json_data)

with open('test.json', 'w') as file:
    json.dump(json_data, file)