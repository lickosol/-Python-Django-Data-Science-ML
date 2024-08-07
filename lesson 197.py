'''
Создайте любой словарь, используя ключи с значениями разных типов
Конвертируйте словарь в JSON
Результирующий JSON выведите в терминал
Выведите в терминал тип результирующего значения
'''
import json

characters = {
    'name': 'Vova Adidas',
    'age': 15,
    'pacan': True,

}

json_ex = json.dumps(characters)

print(json_ex)
print(type(json_ex))