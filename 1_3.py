procent = int (0)
for procent in range(0, 101):
    if (procent - 1) % 10 == 0 and procent != 11:
        print(procent, "Процент")
    elif (procent - 2) % 10 == 0 and procent != 12:
        print(procent, "Процента")
    elif (procent - 3) % 10 == 0 and procent != 13:
        print(procent, "Процента")
    elif (procent - 4) % 10 == 0 and procent != 14:
        print(procent, "Процента")
    else:
        print(procent, "Процентов")