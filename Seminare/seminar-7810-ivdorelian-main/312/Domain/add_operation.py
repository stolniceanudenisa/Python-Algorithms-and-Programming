from Domain.entity import Entity
from Domain.undo_redo_operation import UndoRedoOperation
from Repository.repository import Repository


class AddOperation(UndoRedoOperation):

    def __init__(self,
                 repository: Repository,
                 added_entity: Entity):
        self.repository = repository
        self.added_entity = added_entity

    def undo(self):
        self.repository.delete(self.added_entity.id_entity)

    def redo(self):
        self.repository.create(self.added_entity)
        