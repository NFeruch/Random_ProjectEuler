current_year = 1900
months = {'January': 31, 'February': 28, 'March': 31,
          'April': 30, 'May': 31, 'June': 30,
          'July': 31, 'August': 31, 'September': 30,
          'October': 31, 'November': 30, 'December': 31}
current_month = 'January'
day_in_current_month = 1


def is_leap_year(year):
    if year % 4 == 0:
        return True
    return False


for month in months:
    day = 1
    for i in range(months[month]):
        print(day, end=' ')
        day += 1
    print()
