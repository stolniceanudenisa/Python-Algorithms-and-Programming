from Domain.Grade import Grade


class gradeValidator:
    def validate(self, grade: Grade):
        """
        Validates data regarding Obiect2 and returns any errors
        :param Obiect2: the object to be validated
        :return: errors if they exist
        """
        errors = []
        if grade.value < 1 or grade.value > 10:
            errors.append("Invalid grade")
        if errors:
            return ValueError(errors)
