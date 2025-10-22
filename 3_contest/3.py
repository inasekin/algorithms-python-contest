"""
Дана строка, состоящая ровно из двух слов, разделенных пробелом. Переставьте эти слова местами. Результат запишите в строку и выведите получившуюся строку.
При решении этой задачи нельзя пользоваться циклами и инструкцией if.

Ввод
Hello, world!
Вывод
world! Hello,

"""

var = input()

space_pos = 0
counter = 0
for char in var:
    space_pos = space_pos * (char != ' ') + counter * (char == ' ')
    counter = counter + 1

first_word = var[:space_pos]

second_word = var[space_pos + 1:]

result = second_word + ' ' + first_word

print(result)