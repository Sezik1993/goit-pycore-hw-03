# task 1

from datetime import datetime

def get_days_from_today(date):
    object_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()

    difference = current_date - object_date
   
    return difference.days

print(get_days_from_today("2020-12-09"))



# task 2

import random

def get_numbers_ticket(min, max, quantity):
    lottery_numbers = random.sample(range(min, max), quantity)
    return sorted(lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 36, 5)

print("Ваші лотерейні числа:", lottery_numbers)



# task 3

import re

raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone_number(phone):
    digits = re.sub(r'\D', '', phone)  
    if digits.startswith('380'):
        return f'+{digits}'
    elif digits.startswith('0'):
        return '+38' + digits
    elif digits.startswith('80'):
        return '+3' + digits
    elif digits.startswith('+380'):
        return digits
    else:
        return 'Invalid number'

sanitized_numbers = [normalize_phone_number(num) for num in raw_numbers]
print(sanitized_numbers)



# task 4

from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.06.19"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

def get_upcoming_birthdays(users):
    today = datetime.now().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5: 
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6: 
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


print("Список привітань на цьому тижні:", get_upcoming_birthdays(users))