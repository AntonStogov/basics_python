import re

def parsing_email(email):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not re_email.match(email):
        raise ValueError(f'Ошибка в e-mail адресе: {email}')
    print(re_email.match(email).groupdict())

for i in ['mail@yandex.ru', 'mai@list@yandexru', 'bk@gmail_com', 'mail@astogov.com', 'uag@mail,com']:
    try:
        parsing_email(i)
    except ValueError as err:
        print(err)