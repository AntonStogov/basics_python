def thesaurus(*args):
    names = {}
    for i in sorted(args):
        keys = i[0]
        if keys in names:
            names[keys] += [i]
        else:
            names[keys] = [i]
    return names

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Антон", "Ксения", "Анастасия", "Надежда", "Артур"))
