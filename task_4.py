"""Завдання 4"""
from datetime import datetime as dtdt
from datetime import timedelta


def get_upcoming_birthdays(users):
    upcoming_birthdays = []
    current_date = dtdt.today().date()
    for user in users:
        user_birthday = dtdt.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = dtdt(
            current_date.year, user_birthday.month, user_birthday.day
        ).date()
        if birthday_this_year < current_date:
            birthday_this_year = dtdt(
                current_date.year + 1, user_birthday.month, user_birthday.day
            ).date()
        days_until_birthday = (birthday_this_year - current_date).days
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.13"},
    {"name": "Jane Smith", "birthday": "1990.01.24"},
    {"name": "Karl Dom", "birthday": "1995.01.25"},
    {"name": "Tik Tok", "birthday": "1995.01.26"},
    {"name": "Anton Ptushkin", "birthday": "1995.01.27"},
    {"name": "Face Book", "birthday": "1995.01.28"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
