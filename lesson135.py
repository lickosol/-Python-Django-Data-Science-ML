'''
Создайте функцию image _info с одним параметром типа dict
Функция ожидает словарь, в котором должно быть как минимум два ключа:
image_ id
image_title
Функция должна возвращать строку такого вида
"Image 'my cat' has id 5136"
Если хотя бы одного из этих ключей в словаре нет, функция должна генерировать ошибку TypeError
Вызовите функцию и корректно обработайте ошибку в случае возникновения
'''


def image_info(img):

    if ('image_id' not in img) or ('image_title' not in img):
        raise TypeError("smt empty")

    return f"Image {img['image_title']} has id {img['image_id']}"

print(image_info({'image_title': list(map(str, input().split())), 'image_id': list(map(str, input().split()))}))
# здесь ошибки не будет

print(image_info({'image_title': list(map(str, input().split()))})) #пример с ошибкой
