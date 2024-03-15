import datetime
class ValidationError(Exception):
    pass

class BookValidator:

    def __init__(self):
        self.__errors = None
    def validate(self,book):
        self.__errors = ""
        if book.getID()<0:
            self.__errors += "Invalid book ID!\n"
        if book.getAuthor() == "":
            self.__errors += "Invalid author!\n"
        if book.getTitle() == "":
            self.__errors += "Invalid title!\n"
        if len(self.__errors):
            raise ValidationError(self.__errors)

class ClientValidator:
    def __init__(self):
        self.__errors = None
    def validate(self,client):
        self.__errors = ""
        if client.getID()<0:
            self.__errors += "Invalid client ID!\n"
        if client.getName() == "":
            self.__errors += "Invalid client name!\n"
        if len(self.__errors):
            raise ValidationError(self.__errors)

class RentalValidator:
    def __init__(self):
        self.__errors = None
    def validate(self,rental):
        self.__errors = ""
        if rental.getID()<0:
            self.__errors += "Invalid rental ID!\n"
        #book/client IDs are already validated
        if rental.getRentDate() < datetime.date(1999,1,1):
            self.__errors += "Invalid rent date! This library didn't even exist before 1999!\n"
        if rental.getRentDate() >= datetime.date(3000,1,1):
            self.__errors += "Invalid rent date! That's too far away for these applications to still be used!\n"
        if rental.getReturnDate() is not None:
            if rental.getReturnDate() < datetime.date(1999, 1, 1):
                self.__errors += "Invalid return date! This library didn't even exist before 1999!\n"
            if rental.getReturnDate() >= datetime.date(3000, 1, 1):
                self.__errors += "Invalid return date! That's too far away for these applications to still be used!\n"
            if rental.getRentDate() > rental.getReturnDate():
                self.__errors += "Invalid return date! Return date is before rent date!\n"
        if len(self.__errors):
            raise ValidationError(self.__errors)



# These can be used when the date is not a datetime.date object
class DateError(Exception):
    pass

class DateValidator:

    @staticmethod
    def monthCheck(month):
        if 0 < month <= 12:  ## If month is between 1 and 12, return True.
            return 1
        return "Month is not between 1 and 12!"

    @staticmethod
    def dayCheck(month, day):
        monthList1 = [1, 3, 5, 7, 8, 10, 12]  ## monthList for months with 31 days.
        monthList2 = [4, 6, 9, 11]  ## monthList for months with 30 days.
        monthList3 = 2  ## month with month with 28 days.
        for mon in monthList1:  ## iterate through monthList1.
            if month == mon:  ## Check if the parameter month equals to any month with 31 days.
                if 1 <= day <= 31:  ## If the parameter day is between 1 and 31, return True.
                    return 1
                return "Day is not between 1 and 31!"
        for mon in monthList2:  ## iterate through the monthList with 30 days.
            if month == mon:  ## check if the parameter month equals to any month with 30 days.
                if 1 <= day <= 30:  ## if the parameter day is between 1 and 30,return True.
                    return 1
                return "Day is not between 1 and 30!"
        if month == monthList3:  ## check if parameter month equals month with 28 days.
            if 1 <= day <= 28:  ## if the parameter day is between 1 and 28,return True.
                return 1
            return "Day is not between 1 and 28!"

    @staticmethod
    def yearCheck(year):
        if 1 <= len(year) <= 4:  ## Check if year has between 1 to 4 numbers and return True.
            return 1
        return "The year doesn't have between 1 and 4 digits!"

    def dateCheck(self,date):
        errors = ""
        month, day, year = date.split("/")  ## split the date into 3 separate variables
        ok1 = self.monthCheck(int(month))
        if ok1 != 1:
            errors += ok1 + '\n'
        else:
            ok1 = self.dayCheck(int(month), int(day))
            if ok1 != 1:
                errors += ok1 + '\n'
        ok2 = self.yearCheck(year)
        if ok2 != 1:
            errors += ok2 + '\n'
        if len(errors)>0:
            print(errors)
            raise DateError(errors)
