from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Grade(Entity):
    value: int
    examinee: str

    def __str__(self):
        return f'ID = {self.id_entity},value = {self.value}, ' \
               f'name = {self.examinee} '

    def __repr__(self):
        return str(self)
