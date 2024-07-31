'''
напечатайте в терминал значения «1920х1080» если у этого кортежа длина 2 и значения обоих элементов этo
 строки иначе выведите в терминал «некорректное форматирование изображения» при помощи if else
 чтобы результат совпадал с кодом

с помощью тернарного оператора можно было проверить длину строки. если длина строки >20
 то вывести “string is long” если меньше “string is short”
'''

#код к задаче
'''
my_img = ('1920', '1080')
info = f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else "Incorrect image formatting"
print(info)
'''
'''
my_img = ('1920', '1080')

if len(my_img) == 2:
    print(f"{my_img[0]}x{my_img[1]}")
else: print("Incorrect image formatting")
'''

#2
str = input()

info = f"string is long" if len(str) > 20 else f"string is short"
print(info)