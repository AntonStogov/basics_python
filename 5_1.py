def odd_nums(a, b):
    for i in range(a, b + 1):
        yield int(i)

for n in odd_nums(1, int(input('Введите второе число: '))):
    if n % 2 != 0:
        print(n, end=', ')