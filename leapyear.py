# is this year are leap-year?
def leap(year):
    if (year % 4 == 0) and ((year % 4 == 0) or (year % 400 == 0)):
        print('leap year')
    else:
        print('not leap year')
leap(2000)