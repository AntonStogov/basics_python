from random import choice, randrange

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "лошадь", "завод", "дорога", ]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "в среду", "год", "утром"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "жесткий", "красный", "сердитый"]
def jokes (n, repeat=False):
    """
    Функция позволяет сформировать случайные шутки, собранные из трех списков разных слов

    :param n: количество шуток
    :param repeat: уникальные/неуникальные
    :return: список случайных шуток
    """
    no, adv, adj = nouns.copy(), adverbs.copy(), adjectives.copy()
    list_of_j = []
    list_min = min(no, adv, adj)

    while n and len(list_min):
        num = randrange(len(list_min))
        if repeat:
            list_of_j.append(f"{no.pop(num)} {adv.pop(num)} {adj.pop(num)}")
        else:
            list_of_j.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return list_of_j
print(jokes(100))