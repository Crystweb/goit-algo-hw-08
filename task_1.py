# Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи
# з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній
# сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

import heapq


def minimize_cost(cables):
    heapq.heapify(cables)  # Створення мінімальної піраміди з довжин кабелів
    total_cost = 0

    while len(cables) > 1:
        # Вилучаємо два найменші кабелі
        shortest1 = heapq.heappop(cables)
        shortest2 = heapq.heappop(cables)

        # Об'єднуємо кабелі та додаємо витрати
        combined_length = shortest1 + shortest2
        total_cost += combined_length

        # Додаємо об'єднаний кабель до піраміди
        heapq.heappush(cables, combined_length)

    return total_cost


# Приклад використання
cables = [8, 4, 6, 12]  # Довжини кабелів
min_cost = minimize_cost(cables)
print("Мінімальні витрати на об'єднання кабелів:", min_cost)

