from Domain.Session import Session


class SessionValidator:
    def validate(self, session: Session):
        """
        Validates data regarding session and returns any errors
        :param session: the object to be validated
        :return: errors if they exist
        """
        errors = []
        if session.number_of_students <= 0:
            errors.append("Invalid number of students")
        if len(session.grades) != session.number_of_students:
            errors.append("Not enough students or grades")
        if errors:
            return ValueError(errors)
