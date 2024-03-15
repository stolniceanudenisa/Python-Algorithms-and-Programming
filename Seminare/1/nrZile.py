import datetime

def isLeapYear(year):
    '''
    determina daca un an este bisect
    :param year: nr. intreg
    :return: True daca year este bisect si False in caz contrar
    '''
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def noDaysInMonth(month, year):
    '''
    determina cate zile are o luna dintr-un anumit an
    :param month: nr. intreg
    :param year: nr. intreg
    :return: nr. de zile pe care le-a avut luna month in anul year - nr. intreg
    '''
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    return 30

def dateDifference(oldYear, oldMonth, oldDay, newYear, newMonth, newDay):
    '''
    determina diferenta, in zile, a doua dtae calendaristice
    :param oldYear: nr. intreg
    :param oldMonth: nr. intreg
    :param oldDay: nr. intreg
    :param newYear: nr. intreg
    :param newMonth: nr. intreg
    :param newDay: nr. intreg
    :return: nr. intreg
    '''
    sum = 0
    if oldYear < newYear:
        # anii intregi
        for year in range(oldYear + 1, newYear):
            if isLeapYear(year):
                sum += 366
            else:
                sum += 365

        # lunile intregi din anul din trecut
        for month in range (oldMonth + 1, 13):
            sum += noDaysInMonth(month, oldYear)
        # zilele ramase din luna din trecut
        for day in range(oldDay, noDaysInMonth(oldMonth + 1, oldYear)):
            sum += 1

        # lunile intregi din anul curent
        for month in range(1, newMonth):
            sum += noDaysInMonth(month, oldYear)
        # zilele ramase din luna curenta
        for day in range (1, newDay + 1):
            sum += 1
    else:
        if oldMonth < newMonth:
            # lunile intregi
            for month in range(oldMonth + 1, newMonth):
                sum += noDaysInMonth(month, oldYear)

            # zilele ramase din luna din trecut
            for day in range(oldDay, noDaysInMonth(oldMonth, oldYear) + 1):
                sum += 1
            # zilele ramase din luna curenta
            for day in range(1, newDay):
                sum += 1
        # data din trecut se afla in acelasi an si aceeasi luna cu cea curenta
        else:
            #zilele ramase
            for day in range(oldDay, newDay):
                sum += 1
    return sum

def main():
    zi = int(input("zi="))
    luna = int(input("luna="))
    an=int(input("an="))
    trecut = datetime.datetime(an, luna, zi)
    today = datetime.datetime.now()
    print(dateDifference(trecut.year, trecut.month, trecut.day, today.year, today.month, today.day))
    print((today - trecut).days)

main()