'''
Создайте функцию route_info, которой будет передаваться словарь.
Если в словаре есть ключ distance и его значение - целое число, верните строку "Distance to your
destination is ‹ distance>"
Иначе, если в словаре есть ключи speed и time, верните
строку "Distance to your destination is ‹ speed * time>"
Иначе верните строку "No distance info is available"
Вызовите функцию несколько раз с разными аргументами
'''
def route_info(route):
    if 'distance' in route and isinstance(route['distance'], int):
        return f"Distance to your destination is {route['distance']}"
    if 'speed' in route and 'time' in route:
        return f"Distance to your destination is {route['speed'] * route['time']}"
    else:
        return f"No distance info is available"


print(route_info({'distance': int(input())}))
#здесь сразу вводим целое число, так как питон input() распознает как строка, а это противоречит нашему условию
print(route_info({'distance': input(), 'speed': int(input()), 'time': int(input())}))
#здесь мы скорость и время обязаны ввести целочисленными иначе
# произойдет ошибка "can't multiply sequence by non-int of type 'str'"
print(route_info({'speed': 60}))  # No distance info is available
print(route_info({}))  # No distance info is available
