"""
INSTRUCTIONS
    You are given an initial date as a string in the format YYYY-MM-DD, along with an integer n which represents a number of days. Your task is to calculate the date after adding the given number of days to the initial date and return the result in the YYYY-MM-DD format.

    Keep these points in mind when resolving the task:

    The initial date string is always valid, formatted as YYYY-MM-DD, where YYYY denotes the year, MM the month, and DD the day.
    The given integer n is the number of days you have to add to the initial date and will be up to 50,000.
    The output should be a string showcasing the final date after adding n days, in the YYYY-MM-DD format.
    Your function will be in the form add_days(date: str, n: int) -> str.

CONSTRAINTS

    date = the date string in the YYYY-MM-DD format. The year YYYY will be from 1900 to 2100, inclusive. The month MM and the day DD will be valid for the given year.
    n = the integer representing the number of days you have to add to the initial date. n ranges from 1 to 50,000, inclusive.
    You should consider leap years in the calculation. A year is a leap year if it is divisible by 4, but century years (years divisible by 100) are not leap years unless they are divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.
    The month and day result should always be two digits long, padding with a 0 if necessary. For example, July 9th should be formatted as "07-09".

EXAMPLE
    For date = '1999-01-01' and n = 365, the output should be '2000-01-01'.
"""

def add_days(date, n):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = map(int, date.split('-'))

    def get_days_in_month(month, year):
        if is_leap_year(year) and month == 2:
            return 29
        return days_in_month[month - 1]

    while n > 0:
        days_in_current_month = get_days_in_month(month, year)

        if day + n <= days_in_current_month:
            day += n
            n = 0
        else:
            n -= (days_in_current_month - day + 1)
            day = 1
            month += 1

            if month > 12:
                month = 1
                year += 1

    return f'{year:04d}-{month:02d}-{day:02d}'

# Função para verificar se o ano é bissexto
def is_leap_year(year):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


print(add_days('1999-12-05', 888))  # Expected: '2002-05-11'

