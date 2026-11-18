"""ЛР7, задание B: три квадратичные сортировки.

Все функции возвращают НОВЫЙ список и не меняют исходный.
Внутри нельзя использовать sorted, .sort(), min, max и другие готовые
функции сортировки/поиска минимума.
"""

from __future__ import annotations


def bubble_sort(nums: list[int]) -> list[int]:
    """Новый список, отсортированный по возрастанию. Исходный не меняется.

    На каждом проходе сравниваем соседние элементы и меняем их местами,
    если они стоят не по порядку. Если за проход не было обменов, список
    уже отсортирован — выходим досрочно.

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([2, 2, 1]) -> [1, 2, 2]
    bubble_sort([]) -> []
    """
    result = list(nums)
    n = len(result)

    for end in range(n - 1, 0, -1):
        swapped = False
        for i in range(end):
            if result[i] > result[i + 1]:
                result[i], result[i + 1] = result[i + 1], result[i]
                swapped = True
        if not swapped:
            break

    return result


def insertion_sort(nums: list[int]) -> list[int]:
    """Тот же контракт, что у bubble_sort.

    Берём очередной элемент и сдвигаем его влево, пока он не встанет
    на своё место. На почти отсортированных данных работает почти за O(n).

    insertion_sort([3, 1, 2]) -> [1, 2, 3]
    insertion_sort([2, 2, 1]) -> [1, 2, 2]
    insertion_sort([]) -> []
    """
    result = list(nums)

    for i in range(1, len(result)):
        value = result[i]
        j = i - 1
        while j >= 0 and result[j] > value:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = value

    return result


def selection_sort(nums: list[int]) -> list[int]:
    """Тот же контракт, что у bubble_sort.

    Находим минимум в оставшейся части списка и ставим его на текущее
    место. Минимум ищем вручную, без встроенной min().

    selection_sort([3, 1, 2]) -> [1, 2, 3]
    selection_sort([2, 2, 1]) -> [1, 2, 2]
    selection_sort([]) -> []
    """
    result = list(nums)

    for i in range(len(result) - 1):
        min_index = i
        for j in range(i + 1, len(result)):
            if result[j] < result[min_index]:
                min_index = j
        if min_index != i:
            result[i], result[min_index] = result[min_index], result[i]

    return result
