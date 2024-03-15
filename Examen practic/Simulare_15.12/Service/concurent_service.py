from Repo.concurent_repo import ConcurentFileRepo


class ConcurentService:
    def __init__(self,concurent_repo:ConcurentFileRepo):
        self.__concurent_repo=concurent_repo



    def cautare_dupa_sponsor(self,sponsor_dorit):
        """
        returneaza o lista cu toti concurentii ce apartin aceluiasi sponsor
        :param sponsor_dorit: string
        :return:
        """
        concurenti=self.__concurent_repo.get_all()
        concurenti_doriti=[]
        for concurent in concurenti:
            if concurent.get_sponsor_concurent() == sponsor_dorit:
                concurenti_doriti.append(concurent)


        return concurenti_doriti


