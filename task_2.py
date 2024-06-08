# Дано k відсортованих списків цілих чисел. Ваше завдання — об'єднати їх у один відсортований список. Тепер при
# виконанні завдання ви повинні використати мінімальну купу для ефективного злиття кількох відсортованих списків
# в один відсортований список. Реалізуйте функцію merge_k_lists, яка приймає на вхід список відсортованих списків
# та повертає відсортований список.

import heapq


def merge_k_lists(lists):
    merged_list = []
    min_heap = []

    # Додаємо перший елемент кожного списку до мінімальної купи
    for i, lst in enumerate(lists):
        if lst:  # Перевірка чи список не пустий
            heapq.heappush(min_heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)

    while min_heap:
        val, list_index, element_index = heapq.heappop(min_heap)
        merged_list.append(val)

        # Якщо є ще елементи в поточному списку, додати їх до купи
        if element_index + 1 < len(lists[list_index]):
            next_val = lists[list_index][element_index + 1]
            heapq.heappush(min_heap, (next_val, list_index, element_index + 1))

    return merged_list


# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6], [13, 30], [22, 66]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
