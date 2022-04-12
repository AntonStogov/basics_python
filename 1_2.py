# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
cubed_numbers = []
summa_cubed_numbers = 0  # сумма чисел из списка которые нацело делятся на 7.
for numbers in range(1, 1000, 2):  # c помощью цикла for и функции range перебираем каждое второе число с 1 до 999
    cubed_numbers.append(numbers ** 3)  # с каждым шагом добавляем в конец списка число в кубе
# print(cubed_numbers) использовал для формирования списка

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
for ind, cubed_cell in enumerate(cubed_numbers):  # c помощью цикла мы будем искать суммы, подходящих нам чисел, а перебирать все числа списка поможет функция enumerate()
    sum_numbers = 0  # находится вне цикла wlile для обнуления перед новым шагом
    while cubed_cell > 0:  # пока числа больше нуля выполняем цикл
        sum_numbers += cubed_cell % 10  # берем из примера число 6859 используем оператор % деление на 10 с остатком, остаток будет 9
        cubed_cell //= 10  # делим без остатка с помощью // из 6859 получаем 685.9 отсекаем дробное, повторяем цикл с 685
    if sum_numbers % 7 == 0:  # если конечный результат делится на 7 без остатка, т.е равен нулю
        summa_cubed_numbers += cubed_numbers[ind]  # подходящие нам суммируем и записываем в переменную
print(summa_cubed_numbers) # выводим конечный результат

# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
#  * Решить задачу под пунктом b, не создавая новый список

for ind in range(len(cubed_numbers)):  # снова делаем цикл используем функции range и len указывает длину списка, в нашем случае количество итераций
    cubed_numbers[ind] += 17  # добавляем каждому числу 17
summa_cubed_numbers = 0  # обнуляем сумму кубовых чисел для новых расчетов

#  повторяем часть кода из решения пункта a
for ind, cubed_cell in enumerate(cubed_numbers):
    sum_numbers = 0
    while cubed_cell > 0:
        sum_numbers += cubed_cell % 10
        cubed_cell //= 10
    if sum_numbers % 7 == 0:
        summa_cubed_numbers += cubed_numbers[ind]
print(summa_cubed_numbers)

