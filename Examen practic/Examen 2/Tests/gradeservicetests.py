from Domain.Grade import Grade
from Service.gradeservice import gradeService


def test_add_grade(service: gradeService):
    service.add_grade("""write here data""")
    list_objects = service.get_all_grade()

    assert len(list_objects)


def test_get_grade(service: gradeService):
    grade_1 = service.get_grade('test_id')

    assert grade_1 is None

    list_objects = service.get_all_grade()
    grade_2 = list_objects[0]

    assert isinstance(grade_2, Grade)


def test_update_grade(grade_service: gradeService):
    list_objects = grade_service.get_all_grade()
    old_grade = list_objects[0]
    new_grade = Grade("""write here data""")

    grade_service.update_grade(""" write here data""")

    updated_grade = grade_service.get_grade(new_grade.id_entity)

    assert new_grade == updated_grade
    assert old_grade != updated_grade


def test_delete_grade(grade_service: gradeService):
    list_of_grades = grade_service.get_all_grade()
    grade_service.delete_grade(list_of_grades[0].id_entity)
    list_after_delete = grade_service.get_all_grade()

    assert list_of_grades != list_after_delete
