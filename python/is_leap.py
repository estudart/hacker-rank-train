def is_leap(year):
    leap = None
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            if year % 400 != 0:
                leap = False
                return leap
        return leap
    else:
        leap = False
        return leap