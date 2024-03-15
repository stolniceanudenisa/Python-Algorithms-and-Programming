from typing import Optional, List
from uuid import uuid4

from Domain.Grade import Grade
from Domain.gradevalidator import gradeValidator
from Repository.json_repository import JsonRepository


class gradeService:
    def __init__(self,
                 graderepository: JsonRepository,
                 gradevalidator: gradeValidator,):
        self.graderepository = graderepository
        self.gradevalidator = gradevalidator

    def add_grade(self, grade_value: int, name):
        """
        Adds grade to the repository
        :param grade_value: value of grade
        :param name: name of examinee
        :return: -
        """
        id_grade = str(uuid4())
        grade = Grade(id_grade, grade_value, name)
        self.gradevalidator.validate(grade)
        self.graderepository.create(grade)

    def get_grade(self, grade_id) -> Optional[Grade]:
        """
        Gets a specific grade
        :param grade_id: the id of the object
        :return: the object with the specified id
        """
        return self.graderepository.read(grade_id)

    def get_all_grade(self) -> List[Grade]:
        """
        Returns a list of all grade
        :return: the list of grade
        """
        return self.graderepository.read()
