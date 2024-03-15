from Domain.student_validator import StudentValidator
from Repository.student_file_repository import StudentFileRepo
from Service.student_service import StudentService
from UI.console import Console


def main():
    student_repo = StudentFileRepo('studenti.txt')
    student_validator = StudentValidator()
    student_service = StudentService(student_repo, student_validator)

    console = Console(student_service)
    console.run_ui()


if __name__ == '__main__':
    # Teste()
    main()

# 1,ana,10,8
# 2,bea,5,8
# 3,maria,6,7
# 4,alex,2,8
# 5,alina,3,6
# 6,ela,3,10
# 7,mihai,8,10
# 8,marius,3,10
#
#
# p=5
# b=2
#
#
# 1,ana,10,10
# 2,bea,5,10
# 3,maria,6,9
# 4,alex,2,8
# 5,alina,3,6
# 6,ela,3,10
# 7,mihai,8,10
# 8,marius,3,10
#
#
#
#
# 1,ana,10,10        1,10
# 2,bea,5,10	    2,10
# 3,maria,6,9        3,9
