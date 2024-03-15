class CafeaValidator:
    def validate(self, cafea):
        """
        Clasa pentru validarea unei cafele
        :param cafea: cafeaua validata
        :return:
        """
        erori = []

        if len(cafea.nume_cafea) < 3:
            erori.append('Numele trebuie sa aiba cel putin 3 litere!')
        if not cafea.nume_cafea[0].isupper():
            erori.append('Numele trebuie sa inceapa cu litera mare!')

        if float(cafea.pret_cafea) <= 0:
            erori.append('Pretul trebuie sa fie un float mai mare decat zero!')

        # if cafea.id_cafea == ' ':
        #     erori.append('Id-ul trebuie sa fie nevid!')

        if len(erori) > 0:
            erori_string = '\n'.join(erori)
            raise ValueError(erori_string)
