"""ЛР7, задание A: линейный и бинарный поиск, Two Sum."""

from __future__ import annotations


def linear_search(nums: list[int], x: int) -> int:
    """Индекс первого вхождения x или -1.

    Список может быть любым: линейному поиску сортировка не нужна.

    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    linear_search([], 1) -> -1
    """
    for index, value in enumerate(nums):
        if value == x:
            return index
    return -1


def binary_search(sorted_nums: list[int], x: int) -> int:
    """Индекс x в отсортированном по возрастанию списке или -1.

    Возвращается индекс любого вхождения, если x встречается несколько раз.
    На неотсортированном списке результат не определён.

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    binary_search([5], 5) -> 0
    binary_search([], 5) -> -1
    """
    lo = 0
    hi = len(sorted_nums) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        value = sorted_nums[mid]

        if value == x:
            return mid
        if value < x:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.

    Перебирает все пары, поэтому работает за O(n²).

    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """То же, что two_sum_brute, но за один проход со словарём.

    В словаре храним «значение -> индекс». Для очередного nums[i] проверяем,
    встречалось ли уже target - nums[i]. Проверка ``in`` у словаря идёт
    в среднем за O(1), поэтому весь алгоритм — O(n).

    two_sum_fast([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_fast([1, 2], 10) -> None
    """
    seen: dict[int, int] = {}

    for index, value in enumerate(nums):
        need = target - value
        if need in seen:
            return (seen[need], index)
        # Если значение уже встречалось, оставляем первый индекс:
        # так ответ стабильнее, хотя по заданию допустим любой.
        if value not in seen:
            seen[value] = index

    return None
