import re


class StudentValidator:
    def validate(self, student):
        erori = []
        numele = student.nume_student
        cuv1 = re.split(" ", student.nume_student)[0]
        cuv2 = re.split(" ", student.nume_student)[1]
        if len(cuv1) < 3 or len(cuv2) < 3:
            erori.append('Cele doua numele trebuie sa aiba cel putin 3 caractere!')

        if float(cafea.pret_cafea) < 0:
            erori.append('Pretul trebuie sa fie un numar intreg pozitiv!')

        if student.id_student == ' ':
            erori.append('Id-ul trebuie sa fie nevid!')

        if int(student.id_student) < 0:
            erori.append('Id-ul trebuie sa fie numar int!')

        if student.nota < 0 or student.nota > 10:
            erori.append('Nota trebuie sa fie intre 0 si 10!')

        if student.nume_student == ' ':
            erori.append('Numele trebuie sa fie nevid!')

        if len(numele.split()) != 2:
            erori.append('Numele trebuie sa fie format doar din 2 cuvinte si format din spatiu!')

        # if comanda.mod_de_plata not in ['card', 'cash']:
        #     erori.append('Modul de plata trebuie sa fie card sau cash!')

        if len(erori) > 0:
            erori_string = '\n'.join(erori)
            raise ValueError(erori_string)
