"""Завдання 1"""

from datetime import datetime as dtdt


def get_days_from_today(date):
    while True:
        try:
            user_date = dtdt.strptime(date, "%Y-%m-%d")
            current_date = dtdt.today()
            delta_days = user_date - current_date
            return print(delta_days.days)
        except ValueError:
            print("Неправильний формат дати.")
            date = input("Введіть дату в форматі yyyy-mm-dd ще раз: ")


date = input("Введіть дату в форматі yyyy-mm-dd: ")
get_days_from_today(date)
