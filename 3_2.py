numbers = {
    'zero': 'ноль', 'one': 'один', 'two': 'два',
    'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семмь', 'eight': 'восемь',
    'nine': 'девять', 'ten': 'десять'
}
def num_translate_adv(num):
    if num.istitle():
        num = num.lower()  # Если пользователь введет число на агл с большой буквы, прировняем к нижнему регистру
        return (numbers.get(num, 'Невозможно выполнить перевод').title())  # в таком случае приведем первую букву к верхнему регистру
    else:
        return (numbers.get(num, 'Невозможно выполнить перевод'))

print(num_translate_adv(input('Введите число от 0 до 10 на аглийском языке: ')))

