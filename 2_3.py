forecast = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for i, n in enumerate(forecast):
    if n.isdigit():
        forecast[i] = (f'"{int(n):02}"')
    elif n[1:].isdigit():
        forecast[i] = (f'"{n[0]}{int(n[1:]):02}"')
print(forecast)
print(" ".join(forecast))  # конвертируем список в строку разделяя элементы пробелом