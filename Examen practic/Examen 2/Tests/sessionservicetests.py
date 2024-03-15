from Domain.Grade import Grade
from Domain.Session import Session
from Service.sessionservice import sessionService


def test_add_session(service: sessionService):
    grade = Grade()
    service.Graderepository.create(Grade)
    service.add_session(grade.id_entity, """other data""")
    list_objects = service.get_all_session()
    assert len(list_objects)


def test_get_session(service: sessionService):
    session_1 = service.get_session('test_id')
    assert session_1 is None
    list_objects = service.get_all_session()
    session_2 = list_objects[1]
    assert isinstance(session_2, Session)


def test_update_session(service: sessionService):
    list_objects = service.get_all_session()
    new_Grade = Grade('2', """write data here""")
    service.graderepository.create(new_Grade)
    old_session = list_objects[1]
    new_session = Session(old_session.id_entity, new_Grade.id_entity,
                              "write data here")
    service.update_session(old_session.id_entity, new_Grade.id_entity,
                           "write data here")
    updated_session = service.get_session(new_session.id_entity)
    assert new_session == updated_session
    assert old_session != updated_session


def test_delete_session(service: sessionService):
    service.add_session('1', """write data here""")
    list_objects = service.get_all_session()
    service.delete_session(list_objects[1].id)
    list_after_delete = service.get_all_session()
    assert list_objects != list_after_delete
