from typing import List

from Domain.undo_redo_operation import UndoRedoOperation


class UndoRedoService:

    def __init__(self):
        self.undo_list: List[UndoRedoOperation] = []
        self.redo_list: List[UndoRedoOperation] = []

    def do_undo(self):
        if self.undo_list:
            top_operation = self.undo_list.pop()
            top_operation.undo()
            self.redo_list.append(top_operation)

    def do_redo(self):
        if self.redo_list:
            top_operation = self.redo_list.pop()
            top_operation.redo()
            self.undo_list.append(top_operation)

    def clear_redo(self):
        self.redo_list.clear()

    def add_to_undo(self, operation: UndoRedoOperation):
        self.undo_list.append(operation)
