import collections
from typing import Optional, List
from uuid import uuid4

import jsonpickle

from Domain.entity import Entity
from Domain.Session import Session
from Domain.sessionvalidator import SessionValidator
from Repository.json_repository import JsonRepository


class sessionService:
    def __init__(self,
                 sessionrepository: JsonRepository,
                 sessionvalidator: SessionValidator,
                 graderepository: JsonRepository):
        self.sessionrepository = sessionrepository
        self.sessionvalidator = sessionvalidator
        self.graderepository = graderepository

    def add_session(self, nr_students: int, list_grades: list):
        """
        Adds session to the repository
        :param nr_students: number of students
        :param list_grades: list of grades
        :return: -
        """
        id_session = str(uuid4())
        for grades in list_grades:
            grade = self.graderepository.read(grades)
            if grade is None or isinstance(grade, list):
                raise Exception("Grade doesn't exist")

        session = Session(id_session, nr_students, list_grades)
        self.sessionvalidator.validate(session)
        self.sessionrepository.create(session)

    def get_session(self, session_id) -> Optional[Entity]:
        """
        Gets a specific session
        :param session_id: the id of the object
        :return: the object with the specified id
        """
        return self.sessionrepository.read(session_id)

    def get_all_session(self) -> List[Session]:
        """
        Returns a list of all session
        :return: the list of session
        """
        return self.sessionrepository.read()

    def export_json(self, filename):
        """
        Creates a json file that
        :param filename: name of the file
        :return:
        """
        result = {}
        sessions = self.sessionrepository.read()
        for session in sessions:
            arithmetic = 0
            all_grades = session.grades
            for grades in all_grades:
                grade = self.graderepository.read(grades)
                arithmetic = arithmetic + grade.value
            arithmetic = arithmetic // session.number_of_students
            result[session.id_entity] = arithmetic

        with open(filename, 'w') as file:
            file.write(jsonpickle.dumps(result))

    def session_by_students(self) -> list[Session]:
        """
        The function returns a list of sessions ordered by number of students
        :return: the list
        """
        sessions = self.sessionrepository.read()
        right_sessions = sorted(sessions, key=lambda x: x.number_of_students)
        return right_sessions

    def session_by_examinee(self, name: str) -> list[Session]:
        """
        The function returns al list of session that had a grade with a given
        name of an examinee
        :param name: the given name of the examinee
        :return: list of sessions
        """
        sessions = self.sessionrepository.read()
        shit = {
        }
        shit2 = collections.OrderedDict(sorted(shit.items()))
        right_sessions = []
        for session in sessions:
            all_grades = session.grades
            for grades in all_grades:
                grade = self.graderepository.read(grades)
                if grade.examinee == name:
                    right_sessions.append(session)
        return right_sessions
