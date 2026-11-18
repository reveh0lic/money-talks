"""ЛР7, задание D: бенчмарк поиска, сортировок и Two Sum.

Запуск из корня проекта:

    python -m src.lab07.bench

Результат печатается таблицей и сохраняется в data/lab07/bench.csv.
Замеры выполняются через timeit в отдельном процессе, чтобы квадратичную
сортировку на 100 000 элементов можно было прервать по таймауту.
"""

from __future__ import annotations

import argparse
import multiprocessing as mp
import random
import timeit

from src.lab04.io_txt_csv import ensure_parent_dir, write_csv
from src.lab07.search import binary_search, linear_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

HEADER = ("task", "n", "impl", "seconds")

SEED = 42
SORT_SIZES = (1_000, 10_000, 100_000)
SEARCH_N = 100_000
SEARCH_QUERIES = 10_000
TWO_SUM_SIZES = (1_000, 10_000)
TWO_SUM_TARGET = 10**9


def _timed_worker(connection, fn, args) -> None:
    """Выполнить fn(*args) в дочернем процессе и отправить время родителю."""
    try:
        seconds = timeit.timeit(lambda: fn(*args), number=1)
        connection.send(("ok", seconds))
    except BaseException as error:  # noqa: BLE001 - ошибку нужно вернуть родителю
        connection.send(("error", repr(error)))
    finally:
        connection.close()


def measure(fn, *args, timeout: float = 60.0):
    """Измерить один вызов fn(*args) через timeit.

    Возвращает число секунд или строку "> timeout", если вызов не успел
    завершиться. Процесс создаётся заново, поэтому время запуска Python
    в замер не попадает: timeit стартует уже внутри дочернего процесса.
    """
    context = mp.get_context("spawn")
    receiver, sender = context.Pipe(duplex=False)
    process = context.Process(
        target=_timed_worker,
        args=(sender, fn, args),
        daemon=True,
    )

    process.start()
    sender.close()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        receiver.close()
        return f"> {timeout:g}"

    if receiver.poll(1.0):
        status, value = receiver.recv()
        receiver.close()
        if status == "ok":
            return value
        raise RuntimeError(value)

    receiver.close()
    name = getattr(fn, "__name__", repr(fn))
    raise RuntimeError(f"не удалось измерить {name}")


def random_numbers(n: int, low: int = -1_000_000, high: int = 1_000_000) -> list[int]:
    """Случайные числа для сортировок."""
    return [random.randint(low, high) for _ in range(n)]


def make_search_data() -> tuple[list[int], list[int]]:
    """Список из 100 000 чисел и 10 000 запросов (примерно половина есть)."""
    numbers = [random.randint(0, 1_000_000) for _ in range(SEARCH_N)]
    queries = [random.randint(0, 1_000_000) for _ in range(SEARCH_QUERIES)]

    # Каждый второй запрос берём из самого списка, чтобы были и попадания.
    for i in range(0, SEARCH_QUERIES, 2):
        queries[i] = numbers[random.randrange(SEARCH_N)]

    return numbers, queries


def search_many(search_fn, numbers: list[int], queries: list[int]) -> int:
    """Выполнить search_fn для всех запросов и вернуть число найденных."""
    found = 0
    for x in queries:
        if search_fn(numbers, x) != -1:
            found += 1
    return found


def make_two_sum_data(n: int) -> tuple[list[int], int]:
    """Данные, где target гарантированно достигается только последней парой.

    Остальные числа лежат в диапазоне -1000..1000, поэтому ни одно из них
    в сумме с другим не даёт 10^9. Пара спрятана в конце, чтобы перебор
    пар действительно проходил почти все n² вариантов.
    """
    nums = [random.randint(-1_000, 1_000) for _ in range(n)]
    nums[-2] = 10**6
    nums[-1] = TWO_SUM_TARGET - 10**6
    return nums, TWO_SUM_TARGET


def format_seconds(value) -> str:
    """Число секунд с шестью знаками или готовая строка "> 60"."""
    if isinstance(value, str):
        return value
    return f"{value:.6f}"


def print_table(rows: list[tuple]) -> None:
    """Напечатать строки с выравниванием по ширине колонок."""
    table = [HEADER] + [
        [
            format_seconds(value) if column == 3 else str(value)
            for column, value in enumerate(row)
        ]
        for row in rows
    ]
    widths = [max(len(row[i]) for row in table) for i in range(len(HEADER))]

    for row in table:
        line = "  ".join(
            cell.ljust(widths[i]) for i, cell in enumerate(row)
        )
        print(line.rstrip())


def build_rows(timeout: float) -> list[tuple]:
    """Собрать все строки бенчмарка: task, n, impl, seconds."""
    rows: list[tuple] = []

    # Сортировки: для каждого n генерируем данные ОДИН раз и подаём
    # всем алгоритмам один и тот же список.
    for n in SORT_SIZES:
        data = random_numbers(n)
        print(f"sort  n={n:<7} sorted...", flush=True)
        rows.append(("sort", n, "sorted", measure(sorted, data)))

        for fn in (bubble_sort, insertion_sort, selection_sort):
            print(f"sort  n={n:<7} {fn.__name__}...", flush=True)
            rows.append(("sort", n, fn.__name__, measure(fn, data, timeout=timeout)))

    # Поиск: один и тот же отсортированный список и одни и те же запросы.
    numbers, queries = make_search_data()
    sorted_numbers = sorted(numbers)

    print(f"search n={SEARCH_N}  sorted_for_binary...", flush=True)
    rows.append(
        ("search", SEARCH_N, "sorted_for_binary", measure(sorted, numbers, timeout=120))
    )

    print(f"search n={SEARCH_N}  linear...", flush=True)
    rows.append(
        (
            "search",
            SEARCH_N,
            "linear",
            measure(
                search_many, linear_search, sorted_numbers, queries, timeout=300
            ),
        )
    )

    print(f"search n={SEARCH_N}  binary...", flush=True)
    rows.append(
        (
            "search",
            SEARCH_N,
            "binary",
            measure(
                search_many, binary_search, sorted_numbers, queries, timeout=120
            ),
        )
    )

    # Two Sum: target существует, пара спрятана в конце списка.
    for n in TWO_SUM_SIZES:
        data, target = make_two_sum_data(n)
        for fn in (two_sum_brute, two_sum_fast):
            print(f"two_sum n={n:<5} {fn.__name__}...", flush=True)
            rows.append(
                (
                    "two_sum",
                    n,
                    fn.__name__,
                    measure(fn, data, target, timeout=timeout),
                )
            )

    return rows


def parse_args() -> argparse.Namespace:
    """Разобрать аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="Замеры сортировок, поиска и Two Sum для ЛР7."
    )
    parser.add_argument(
        "--out",
        default="data/lab07/bench.csv",
        help="куда сохранить CSV (по умолчанию data/lab07/bench.csv)",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="предел в секундах для одного долгого замера (по умолчанию 60)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Одно зерно на весь бенчмарк: данные воспроизводимы от запуска к запуску.
    random.seed(SEED)

    rows = build_rows(args.timeout)

    print()
    print_table(rows)

    ensure_parent_dir(args.out)
    write_csv(rows, args.out, header=HEADER)
    print(f"\nТаблица сохранена: {args.out}")


if __name__ == "__main__":
    main()
