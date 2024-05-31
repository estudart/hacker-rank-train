year = 2016

def dayOfProgrammer(year):
    # Write your code here

    if year > 1918:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    elif year < 1918:
        if year % 4 == 0:
            return f"12.09.{year}"
        else:
            return f"13.09.{year}"
    else:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return f"25.09.{year}"
        else:
            return f"26.09.{year}"

print(dayOfProgrammer(year=year))