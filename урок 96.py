'''
1.Перепишите вызов функции merge_lists_to_dict из предыдущей задачи так, чтобы в нём использовались аргументы с ключевыми словами
Добавьте ещё один вызов функции, в котором будет один позиционный аргумент, а второй - аргумент с ключевым словом


def merge_lists_to_dict(product, id):
    res = dict(zip(product, id))
    return res


product = list(map(str, input().split()))
id = list(map(int, input().split()))
print(merge_lists_to_dict(product, id))
'''

'''
2. Создайте функцию update_car_info, в которой все
именованные аргументы будут объединяться в
словарь car
Добавьте в словарь новый ключ is_available с значением True
Верните из функции изменённый словарь
Вызовите функцию с именованными аргументами brand и price, их значения могут быть любыми
Выведите в терминал результат функции
'''

def update_car_info(**car):
    car['is_available'] = list(map(str, input().split()))
    return car


car = update_car_info(brand='BMW', price=10000)
print(car)