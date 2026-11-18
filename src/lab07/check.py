"""ЛР7, задание C: проверка функций против эталона.

Запуск из корня проекта:

    python -m src.lab07.check

При расхождении программа падает с AssertionError и показывает данные,
на которых оно произошло. Если всё хорошо, печатается "OK: N проверок".
"""

from __future__ import annotations

import random
from collections.abc import Callable

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

# Счётчик всех выполненных assert-проверок. Нужен только для итогового "OK: N".
CHECKS = 0


def _check(condition: bool, message: str) -> None:
    """Проверить условие и увеличить счётчик проверок."""
    global CHECKS
    CHECKS += 1
    assert condition, message


def check_sorting(fn: Callable[[list[int]], list[int]], trials: int = 100) -> None:
    """Сравнить сортировку fn со sorted на случайных списках.

    Длины от 0 до 50, значения от -100 до 100, поэтому встречаются
    пустые списки, списки из одного элемента, отрицательные числа
    и повторы. Дополнительно проверяется, что исходный список не изменён.
    """
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        expected = sorted(nums)
        result = fn(nums)

        _check(
            result == expected,
            f"{fn.__name__} ошиблась на {nums}: получилось {result}, "
            f"ожидалось {expected}",
        )
        _check(
            nums == original,
            f"{fn.__name__} изменила исходный список: было {original}, "
            f"стало {nums}",
        )


def check_search() -> None:
    """Сравнить linear_search и binary_search с эталоном.

    linear_search проверяем против list.index: он тоже возвращает индекс
    первого вхождения. Для отсутствующего элемента list.index бросает
    ValueError, а linear_search должен вернуть -1.

    binary_search проверяем на отсортированных списках: найденный индекс
    должен указывать на x (любое вхождение), а для отсутствующего x — -1.
    Отдельно проверяются пустой список, один элемент и крайние значения.
    """
    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]

        queries = [random.randint(-120, 120) for _ in range(5)]
        if nums:
            queries.extend([nums[0], nums[-1], min(nums), max(nums)])

        for x in queries:
            expected = nums.index(x) if x in nums else -1
            result = linear_search(nums, x)
            _check(
                result == expected,
                f"linear_search({nums}, {x}) = {result}, ожидалось {expected}",
            )

        sorted_nums = sorted(nums)
        for x in queries + [-101, 101]:
            result = binary_search(sorted_nums, x)
            if x in sorted_nums:
                _check(
                    0 <= result < len(sorted_nums) and sorted_nums[result] == x,
                    f"binary_search({sorted_nums}, {x}) вернул {result}, "
                    f"а не индекс элемента {x}",
                )
            else:
                _check(
                    result == -1,
                    f"binary_search({sorted_nums}, {x}) = {result}, ожидалось -1",
                )

    # Явные краевые случаи: пустой список, один элемент, границы.
    for nums, x, expected in [
        ([], 1, -1),
        ([5], 5, 0),
        ([5], 4, -1),
        ([1, 2], 1, 0),
        ([1, 2], 2, 1),
        ([1, 2], 3, -1),
    ]:
        _check(
            linear_search(nums, x) == expected,
            f"linear_search({nums}, {x}) != {expected}",
        )
        _check(
            binary_search(nums, x) == expected,
            f"binary_search({nums}, {x}) != {expected}",
        )


def check_two_sum(trials: int = 100) -> None:
    """Сравнить two_sum_brute и two_sum_fast между собой.

    При нескольких правильных ответах пары могут отличаться, поэтому
    проверяем не равенство пар, а то, что оба способа одновременно нашли
    ответ или одновременно не нашли, и что найденная пара действительно
    даёт target.
    """
    cases = [
        ([2, 7, 11, 15], 9),
        ([3, 3], 6),
        ([1, 2], 10),
        ([], 0),
        ([5], 10),
        ([-3, 4, 3, 90], 0),
    ]

    for _ in range(trials):
        n = random.randint(0, 40)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)
        cases.append((nums, target))

    for nums, target in cases:
        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        _check(
            (brute is None) == (fast is None),
            f"two_sum на {nums}, target={target}: "
            f"brute={brute}, fast={fast}",
        )

        for name, pair in (("two_sum_brute", brute), ("two_sum_fast", fast)):
            if pair is None:
                continue
            i, j = pair
            _check(
                0 <= i < j < len(nums) and nums[i] + nums[j] == target,
                f"{name}({nums}, {target}) вернул {pair}, "
                f"но nums[{i}] + nums[{j}] != {target}",
            )


def main() -> None:
    """Прогнать все проверки на одном и том же зерне random."""
    random.seed(42)

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
    check_search()
    check_two_sum()

    print(f"OK: {CHECKS} проверок")


if __name__ == "__main__":
    main()
