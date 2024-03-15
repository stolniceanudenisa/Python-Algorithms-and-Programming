from Repo.clasament_repo import ClasamentFileRepo


class ClasamentService:
    def __init__(self,clasament_repo:ClasamentFileRepo):
        self.__clasament_repo=clasament_repo


    def ordonare_clasament(self,lista):
        """

        :return:
        """
        return sorted(lista ,key=lambda d:d[1])



    def clasament(self):
        """
        returneaza un dictionar unde cheia este proba iar valorile sunt castigatorul probei si punctajul
        :return:
        """
        lista_clasament=self.__clasament_repo.get_all()
        lista_castigatori={}
        lista_probe=[]
        maxim=0
        for castigator in lista_clasament:
            proba= castigator.get_denumire_proba()
            lista_probe.append(proba)
        for proba in lista_probe:

            maxim=0
            for castigator in lista_clasament:
                if castigator.get_denumire_proba()== proba:
                    if int(castigator.get_punctaj_concurent()) >maxim:
                        maxim=int(castigator.get_punctaj_concurent())
                        concurent_maxim=castigator.get_id_concurent()
            lista_castigatori[proba]=[concurent_maxim,maxim]
        return lista_castigatori

    def clasament_final(self):
        """
        returneaza din dictionarul clasament doar concurentul ce are suma punctajelor de la toate probele cel mai mare
        :return:
        """
        lista_clasament = self.__clasament_repo.get_all()
        lista_castigatori=self.clasament()
        maxim_castigator=0
        for castigatori in lista_castigatori.values():
            print(castigatori)
            id_concurent=castigatori[0]
            punctaj_concurent=int(castigatori[1])
            for concurent in lista_clasament:
                if concurent.get_id_concurent()==id_concurent:
                    punctaj_concurent+=int(concurent.get_punctaj_concurent())
            if punctaj_concurent >maxim_castigator:
                maxim_castigator =punctaj_concurent
                maxim_concurent=id_concurent

        return self.__clasament_repo.get_by_id(maxim_concurent)


    def print_clasament(self):
        """
        printeaza din lista de castigatori castigatorul probelor
        :return:
        """
        lista_castigatori=self.clasament()
        print(lista_castigatori)
        for castigator in lista_castigatori.values():
            print(self.__clasament_repo.get_by_id(castigator[0]).get_denumire_proba(),self.__clasament_repo.get_by_id(castigator[0]).get_id_concurent())


