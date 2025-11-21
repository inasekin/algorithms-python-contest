# Задача A. Очередь к врачу
# Решение через обычный список (list)
# Подход: моделируем очередь как массив
# "+i" - добавляем пациента i в конец очереди
# "*i" - вставляем пациента i в середину очереди
# "-"  - извлекаем первого пациента из очереди
#
# Примечание: решение простое, но имеет сложность O(N²) из-за
# операций insert() и pop(0), которые работают за O(N).

var = int(input())
queue = []

for _ in range(var):
    command = input().strip().split()

    if command[0] == '+':
        patient_id = int(command[1])
        queue.append(patient_id)
    elif command[0] == '*':
        patient_id = int(command[1])
        mid_pos = (len(queue) + 1) // 2
        queue.insert(mid_pos, patient_id)
    elif command[0] == '-':
        print(queue.pop(0))