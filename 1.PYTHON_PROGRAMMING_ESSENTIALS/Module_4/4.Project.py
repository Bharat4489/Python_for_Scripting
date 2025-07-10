"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if(datetime.MAXYEAR>=year>=datetime.MINYEAR):
        if(13>month>0):
            if month==12:
                no_of_days = 31
            else:
                no_of_days = (datetime.date(year,month+1,1) - datetime.date(year, month,1)).days
    return no_of_days

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
    
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    try:
        if datetime.date(year,month,day):
            return True
        else: 
            return False
        
    except ValueError:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    try:
        first_date = datetime.date(year1, month1, day1)
        last_date = datetime.date(year2, month2, day2)
        if last_date>=first_date:
            return (datetime.date(year2, month2, day2)- datetime.date(year1, month1, day1)).days
        else:
            return 0
        
    except ValueError:
        return 0

def age_in_days(year, month, day):
    """
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    try:
        today = datetime.date.today()
        bday = datetime.date(year,month,day)
        if days_between(bday.year,bday.month,bday.day, today.year,today.month,today.day):
            return days_between(bday.year,bday.month,bday.day,today.year,today.month,today.day)
        else:
            return 0
        
    except ValueError:
        return 0


print(age_in_days(2017,1,1))
print(days_in_month(1,1))
print(days_between(1973, 8, 14, 1973, 8, 13))
print(days_between(20000, 1, 1, 2047, 8, 2))