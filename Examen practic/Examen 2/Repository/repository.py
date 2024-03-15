from typing import Protocol, Type, Union, Optional, List

from Domain.entity import Entity


class Repository(Protocol):
    def create(self, entity: Entity) -> None:
        ...

    def read(self, id_entity: object = None) \
            -> Type[Union[Optional[Entity], List[Entity]]]:
        ...

    def update(self, entity: Entity) -> None:
        ...

    def delete(self, id_entity: str) -> None:
        ...
