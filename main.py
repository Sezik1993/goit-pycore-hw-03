from datetime import datetime

def get_days_from_today(date):
    object_date = datetime.strptime(date, "%Y-%m-%d")
    current_date = datetime.today()

    difference = current_date - object_date
   
    return difference.days

print(get_days_from_today("2020-12-09"))