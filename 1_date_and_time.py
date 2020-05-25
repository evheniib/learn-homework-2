"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад        +
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta
import locale 
locale.setlocale(locale.LC_ALL, "russian")

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()

    #вчера
    delta = timedelta(days=1)
    result = dt_now - delta
    print(result.strftime('%A %d %B %Y'))

    #сегодня
    print(dt_now)

    #30 дней назад
    result = dt_now - delta
    print(result.strftime('%A %d %B %Y'))




def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
      
    dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
