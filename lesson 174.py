'''
Создайте класс Image
У каждого экземпляра класса Image должно быть три собственных атрибута
-resolution
-title
-extension
В классе должен быть метод resize, с помощью которого можно поменять разрешение изображения. Вы должны просто менять значение атрибута resolution
Создайте несколько экземпляров класса Image и вызовите метод resize
'''

class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

my_resolution = Image(f"{1920}x{1080}", str(input()), str(input()))
print(my_resolution.resolution, my_resolution.title, my_resolution.extension)

my_resolution.resize(f"{4000}x{3000}")
print(my_resolution.resolution)

