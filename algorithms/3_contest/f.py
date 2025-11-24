# Носки
#
# Задача: для каждой из M точек найти количество носков, покрывающих эту точку
# Носок покрывает отрезок [l, r] включительно
#
# Решение за O((N + M) log(N + M)) с использованием sweep line:
# 1. Создаем события начала и конца носков
# 2. Сортируем запросы по координатам
# 3. Обрабатываем события по мере продвижения по запросам

L, N, M = map(int, input().split())

# События изменения покрытия
events = []
for _ in range(N):
    l, r = map(int, input().split())
    events.append((l, 0))  # начало носка: +1 к покрытию
    events.append((r + 1, 1))  # конец носка (на r+1): -1 к покрытию

# Сортируем события по координате
events.sort()

# Запросы с сохранением исходного порядка
query_list = []
for i in range(M):
    x = int(input())
    query_list.append((x, i))  # (координата, индекс в выводе)

# Сортируем запросы по координате
query_list.sort()

result = [0] * M
current_coverage = 0  # Текущее количество носков в точке
event_idx = 0

# Обрабатываем запросы в отсортированном порядке
for x, query_idx in query_list:
    # Применяем все события до текущей точки запроса включительно
    while event_idx < len(events) and events[event_idx][0] <= x:
        coord, event_type = events[event_idx]
        if event_type == 0:  # начало носка
            current_coverage += 1
        else:  # конец носка (event_type == 1)
            current_coverage -= 1
        event_idx += 1

    # Сохраняем результат для текущего запроса
    result[query_idx] = current_coverage

# Выводим результаты в исходном порядке запросов
for num in result:
    print(num)