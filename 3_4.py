def thesaurus_adv(*args):
    f_l_names = {}
    for f_l in args:
        f_l_names.setdefault(f_l.split()[1][0], {}).setdefault(f_l.split()[0][0], []).append(f_l)
    return f_l_names

print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Антон Скобелкин",
                "Ксения Целищева", "Анна Савельева", "Надежда Галина", "Артур Галин"))
