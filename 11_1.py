class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 0 <= day <= 31:
            if 0 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Всё работает'
                else:
                    return f'Не верный год'
            else:
                return f'Не верный месяц'
        else:
            return f'Не верный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('01 - 03 - 2022')
print(today)
print(Data.valid(1, 8, 2023))
print(today.valid(32, 9, 2022))
print(today.valid(30, 12, 2022))
print(Data.extract('02 - 03 - 2022'))
print(today.extract('10 - 12 - 2019'))
print(Data.valid(1, 3, 2022))