"""
Подсчет количества уникальных слов, последними написанных каждой командой.
Если слово написали несколько команд, засчитывается только последней.
"""

# Читаем количество команд и предложений
n_teams, n_sentences = map(int, input().split())

# Словарь: слово -> номер команды, которая написала его последней
last_team = {}

# Обрабатываем предложения
for _ in range(n_sentences):
    team_num, word = input().split()
    last_team[word] = int(team_num)

# Подсчитываем количество уникальных слов для каждой команды
counts = [0] * n_teams
for team in last_team.values():
    counts[team - 1] += 1

# Выводим результат
print(' '.join(map(str, counts)))