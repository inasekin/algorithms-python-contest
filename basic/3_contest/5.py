"""
Дана строка, в которой буква h встречается минимум два раза. Удалите из этой строки первое и последнее вхождение буквы h, а также все символы, находящиеся между ними.

Ввод
Вывод

In the hole in the ground there lived a hobbit
In tobbit

Пример 2

Ввод
Вывод
qwertyhasdfghzxcvb

qwertyzxcvb

"""

var = input()
firstH = var.find('h')
lastH = var.rfind('h')
print(var if firstH == lastH or firstH == -1 else var[:firstH] + var[lastH+1:])
