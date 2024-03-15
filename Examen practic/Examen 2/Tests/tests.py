from Service.gradeservice import gradeService
from Tests.sessionservicetests import test_add_session, test_get_session, \
    test_update_session, test_delete_session
from Tests.gradeservicetests import test_add_grade, test_get_grade, \
    test_update_grade, test_delete_grade


def clear_file():
    file = open('tests.json', 'w')
    file.close()


def run_first_tests(gradeservice: gradeService):
    test_add_grade(gradeservice)
    test_get_grade(gradeservice)
    test_update_grade(gradeservice)
    test_delete_grade(gradeservice)
    clear_file()


def run_second_tests(sessionservice: sessionService):
    test_add_session(sessionservice)
    test_get_session(sessionservice)
    test_update_session(sessionservice)
    test_delete_session(sessionservice)
    clear_file()


def run_all_tests(gradeservice: gradeService,
                  sessionservice: sessionService):
    try:
        clear_file()
        run_first_tests(gradeservice)
        clear_file()
        run_second_tests(sessionservice)
        clear_file()
    except AssertionError as ae:
        print("Assertion Error: ", ae)
    except Exception as ex:
        print("Error: ", ex)
