"""
В Государственную Думу Федерального Собрания Российской Федерации выборы производятся по партийным спискам. Каждый избиратель указывает одну партию, за которую он отдает свой голос. В Государственную Думу попадают партии, которые набрали не менее 7% от числа голосов избирателей.

Дан список партий и список голосов избирателей. Выведите список партий, которые попадут в Государственную Думу.
Формат ввода

В первой строке входного файла написано слово PARTIES:. Далее идет список партий, участвующих в выборах.

Затем идет строка, содержащая слово VOTES:. За ним идут названия партий, за которые проголосовали избиратели, по одному названию в строке. Названия могут быть только строками из первого списка.
Формат вывода

Программа должна вывести названия партий, получивших не менее 7% от числа голосов в том порядке, в котором они следуют в первом списке.

Пример 1
Ввод
Вывод

PARTIES:
Party one
Party two
Party three
VOTES:
Party one
Party one
Party three
Party one
Party one
Party three
Party two
Party one
Party three
Party three
Party one
Party one
Party three
Party three
Party one



Party one
Party three

"""

f = open('input.txt', 'r')

f.readline()

parties = []
while True:
    line = f.readline().strip()
    if line == 'VOTES:':
        break
    parties.append(line)

votes = []
for line in f:
    votes.append(line.strip())

f.close()

min_votes = len(votes) * 7 / 100

for party in parties:
    if votes.count(party) >= min_votes:
        print(party)