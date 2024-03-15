class CafeaValidator:

    def validate(self, cafea):
        erori = []
        if cafea.id_cafea == ' ':
            erori.append('Id-ul cafelei trebuie sa fie nevid!')

        if float(cafea.pret_cafea) < 0:
            erori.append('Pretul trebuie sa fie un numar intreg pozitiv!')

        if len(erori) > 0:
            erori_string = '\n'.join(erori)
            raise ValueError(erori_string)
