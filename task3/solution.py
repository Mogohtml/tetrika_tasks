"""
Задание 3: Когда пользователь заходит на страницу урока, мы сохраняем время его захода.
Когда пользователь выходит с урока (или закрывает вкладку, браузер – в общем как-то
разрывает соединение с сервером), мы фиксируем время выхода с урока.
Время присутствия каждого пользователя на уроке хранится у нас в виде интервалов.
В функцию передается словарь, содержащий три списка с таймстемпами (время в секундах):
lesson – начало и конец урока pupil – интервалы присутствия ученика tutor – интервалы
присутствия учителя Интервалы устроены следующим образом – это всегда список из четного
количества элементов. Под четными индексами (начиная с 0) время входа на урок, под нечетными - время
выхода с урока. Нужно написать функцию appearance, которая получает на вход словарь с интервалами
и возвращает время общего присутствия ученика и учителя на уроке (в секундах).
"""

# task3/solution.py

def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']
    pupil_intervals = intervals['pupil']
    tutor_intervals = intervals['tutor']

    pupil_times = set()
    tutor_times = set()

    for i in range(0, len(pupil_intervals), 2):
        start = max(pupil_intervals[i], lesson_start)
        end = min(pupil_intervals[i + 1], lesson_end)
        pupil_times.update(range(start, end))

    for i in range(0, len(tutor_intervals), 2):
        start = max(tutor_intervals[i], lesson_start)
        end = min(tutor_intervals[i + 1], lesson_end)
        tutor_times.update(range(start, end))

    common_times = pupil_times & tutor_times
    return len(common_times)