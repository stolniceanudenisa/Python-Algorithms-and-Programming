from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Session(Entity):
    number_of_students: int
    grades: list

    def __str__(self):
        return f'ID = {self.id_entity}, ' \
               f'nr of students = {self.number_of_students},' \
               f'grades = {self.grades} '

    def __repr__(self):
        return str(self)
