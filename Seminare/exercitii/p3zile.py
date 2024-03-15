'''
    descriere - Determina o data calendaristica (sub forma an, luna, zi) pornind de
    la doua numere întregi care reprezintă anul si numărul de ordine al zilei in anul respectiv.
    input - anul si numarul de ordine al zilei.
    output - o data calendaristica (sub forma an, luna, zi)
'''

import datetime

anul = int(input("Anul: "))
ziua = int(input("Ziua de ordin: "))

x = datetime.datetime(anul, 1, 1) + datetime.timedelta(ziua-1)

print(x.strftime("%Y"), ".", x.strftime("%b"), ".", x.strftime("%d"))    #,sep = ""


# %Y - Year with century as a decimal number.	2013, 2019 etc.
# %b - Abbreviated month name.	Jan, Feb, ..., Dec
# %d - Day of the month as a zero-padded decimal.	01, 02, ..., 31
# https://www.programiz.com/python-programming/datetime/strftime
#A timedelta object represents a duration, the difference between two dates or times. All arguments are optional and default to 0 .
# Arguments may be integers or floats, and may be positive or negative.
# Only days, seconds and microseconds are stored internally.
#datetime – Combination of time and date (Month, day, year, hour, second, microsecond)
#The strftime() method returns a string representing date and time using date, time or datetime object.