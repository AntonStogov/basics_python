numbers = {
    'zero': 'ноль', 'one': 'один', 'two': 'два',
    'three': 'три', 'four': 'четыре', 'five': 'пять',
    'six': 'шесть', 'seven': 'семмь', 'eight': 'восемь',
    'nine': 'девять', 'ten': 'десять'
}
def num_translate(num):
    return (numbers.get(num, 'Невозможно выполнить перевод'))  # Если введено неверное число, программа выведет None Невозможно выполнить перевод

print(num_translate(input('Введите число от 0 до 10 на аглийском языке: ')))
