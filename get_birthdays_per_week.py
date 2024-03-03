import calendar
from collections import defaultdict
from datetime import datetime

birthday_dict = defaultdict(list)
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_birthdays_per_week(users):
    weekdays = list(calendar.day_name)
    current_date = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1)

        delta_days = (birthday_this_year - current_date).days

        if delta_days < 7:
            if birthday_this_year.weekday() >= 5:
                birthday_dict[weekdays[0]].append(name)
            else:
                birthday_dict[weekdays[birthday_this_year.weekday()]].append(name)

    for day, users_list in birthday_dict.items():
        print(f"{day}: {', '.join(users_list)}")


users = [
    {"name": "Bill Gates", "birthday": datetime(1956, 3, 4)},
    {"name": "Jill Valentine", "birthday": datetime(1967, 3, 4)},
    {"name": "Kim Kardashian", "birthday": datetime(1985, 3, 8)},
    {"name": "Jan Koum", "birthday": datetime(1965, 3, 8)},
]

if __name__ == "__main__":
    get_birthdays_per_week(users)
