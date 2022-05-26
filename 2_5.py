# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

# A
prices = [57.8, 46.51, 97, 67.2, 12.21, 81.11, 19, 73.9, 10, 8.1]
print('Решение задачи пункт A:')
for i in prices:
    rub, kop = f"{i:.2f}".split(".")
    print(f'{rub} руб. {kop} коп.,', end=' ')  # Выводим на экран цены в виде n руб n коп

# B
print(f'\nРешение задачи пункт B:')
print(f"ID base: {id(prices)} - {prices}")
prices.sort()
print(f"ID change: {id(prices)} - {prices}")

# C and D
print('Решение задачи пункт С и D:')
price_new = sorted(prices, reverse=True)  # сортируем новый список в порядке возрастания и разворачиваем
print(f'ID change: {id(price_new)} - {price_new}')
print(f'{price_new[:5][::-1]}')  # 5 самых дорогих товаров
