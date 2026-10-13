def format_record(rec: tuple[str, str, float]) -> str:
    if not isinstance(rec, tuple):
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("Запись должна содержать ФИО, группу и GPA")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    if not 0.0 <= gpa <= 5.0:
        raise ValueError("GPA должен быть от 0 до 5")

    fio_parts = fio.split()
    if len(fio_parts) not in (2, 3):
        raise ValueError("ФИО должно состоять из двух или трёх слов")

    group = group.strip()
    if not group:
        raise ValueError("Группа не должна быть пустой")

    surname = fio_parts[0].capitalize()
    initials = "".join(f"{name[0].upper()}." for name in fio_parts[1:])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"