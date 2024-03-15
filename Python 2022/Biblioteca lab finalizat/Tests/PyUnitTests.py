import unittest

from Domain.carte import Carte
from Domain.carte_validator import CarteValidator
from Domain.client import Client
from Domain.inchiriere import Inchiriere
from Repository.carte_file_repository import CarteFileRepository
from Repository.carte_repository import CarteRepository
from Repository.client_file_repository import ClientFileRepository
from Repository.client_repository import ClientRepository
from Repository.inchiriere_repository import InchiriereRepository
from Service.carte_service import CarteService
from Service.client_service import ClientService
from utils import clear_file


class TestCarteDomain(unittest.TestCase):
    def setUp(self):
        from Domain.carte import Carte
        self.carte = Carte('10', 'ion', 'roman', 'lv')

    def test_id(self):
        self.assertTrue(self.carte.get_id_carte() == '10')

    def test_titlu(self):
        self.assertTrue(self.carte.get_titlu_carte() == 'ion')

    def test_descriere(self):
        self.assertTrue(self.carte.get_descriere_carte() == 'roman')

    def test_autor(self):
        self.assertTrue(self.carte.get_autor_carte() == 'lv')

    def test_set_id(self):
        self.carte.set_id_carte('5')
        self.assertTrue(self.carte.get_id_carte() == '5')

    def test_set_titlu(self):
        self.carte.set_titlu_carte('moara')
        self.assertTrue(self.carte.get_titlu_carte() == 'moara')

    def test_set_descriere(self):
        self.carte.set_descriere_carte('nuvela')
        self.assertTrue(self.carte.get_descriere_carte() == 'nuvela')

    def test_set_autor(self):
        self.carte.set_autor_carte('is')
        self.assertTrue(self.carte.get_autor_carte() == 'is')

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class TestClientDomain(unittest.TestCase):
    def setUp(self):
        from Domain.client import Client
        self.client = Client('1', 'Ion Popa', '5220309019075')

    def test_id(self):
        self.assertTrue(self.client.get_id_client() == '1')

    def test_nume(self):
        self.assertTrue(self.client.get_nume_client() == 'Ion Popa')

    def test_cnp(self):
        self.assertTrue(self.client.get_cnp_client() == '5220309019075')

    def test_set_id(self):
        self.client.set_id_client('5')
        self.assertTrue(self.client.get_id_client() == '5')

    def test_set_nume(self):
        self.client.set_nume_client('maria')
        self.assertTrue(self.client.get_nume_client() == 'maria')

    def test_set_cnp(self):
        self.client.set_cnp_client('5220309011111')
        self.assertTrue(self.client.get_cnp_client() == '5220309011111')

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class TestInchiriereDomain(unittest.TestCase):
    def setUp(self):
        self.inchiriere = Inchiriere('1', '2', '3')

    def test_id_inchiriere(self):
        self.assertTrue(self.inchiriere.get_id_inchiriere() == '1')

    def test_id_client(self):
        self.assertTrue(self.inchiriere.get_client_id() == '2')

    def test_id_carte(self):
        self.assertTrue(self.inchiriere.get_carte_id() == '3')

    def test_set_id_inchiriere(self):
        self.inchiriere.set_id_inchiriere('7')
        self.assertTrue(self.inchiriere.get_id_inchiriere() == '7')

    def test_set_id_client(self):
        self.inchiriere.set_client_id('8')
        self.assertTrue(self.inchiriere.get_client_id() == '8')

    def test_set_id_carte(self):
        self.inchiriere.set_carte_id('9')
        self.assertTrue(self.inchiriere.get_carte_id() == '9')

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class CarteRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._carti_repo = CarteRepository()

    def test_add(self):
        carte1 = Carte('333', 'aaa', 'bbb', 'ccc')
        self.assertEqual(self._carti_repo.__len__(), 0)
        self._carti_repo.add(carte1)
        self.assertEqual(self._carti_repo.__len__(), 1)

    def test_get_carti(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'ccc')
        carte2 = Carte('2', 'vvvv', 'zdad', 'sddd')
        carti = {
            '1': carte1,
            '2': carte2
        }
        self._carti_repo.add(carte1)
        self._carti_repo.add(carte2)
        self.assertEqual(self._carti_repo.get_carti(), carti)

    def test_set_carti(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'ccc')
        carte2 = Carte('2', 'bbb', 'eee', 'sddd')
        self._carti_repo.add(carte1)
        self._carti_repo.add(carte2)
        carte3 = Carte('3', 'ccc', 'fff', 'hhh')
        carte4 = Carte('4', 'ddd', "ggg", 'iii')
        carti = {
            3: carte3,
            4: carte4
        }
        self._carti_repo.set_carti(carti)
        self.assertEqual(self._carti_repo.get_carti(), carti)

    def test_get_by_id(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'cccc')
        self._carti_repo.add(carte1)
        self.assertEqual(self._carti_repo.get_by_id('1').get_id_carte(), '1')

    def test_get_by_titlu(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'cccc')
        self._carti_repo.add(carte1)
        self.assertEqual(self._carti_repo.get_by_id('1').get_titlu_carte(), 'aaa')

    def test_get_by_descriere(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'cccc')
        self._carti_repo.add(carte1)
        # self.assertEqual(self._carti_repo.get_by_id('1').get_descriere_carte, 'bbb')

    def test_get_by_autor(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'ccc')
        self._carti_repo.add(carte1)
        # self.assertEqual(self._carti_repo.get_by_id('1').get_autor_carte, 'ccc')

    def test_find(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'cccc')
        self._carti_repo.add(carte1)
        self.assertEqual(self._carti_repo.get_by_id('1'), carte1)
        self.assertEqual(self._carti_repo.get_by_id('2'), None)

    def test_get_all(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'Lvvvcc')
        self._carti_repo.add(carte1)
        self.assertEqual(len(self._carti_repo.get_all()), 1)

    def test_update(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'Lvvvcc')
        self._carti_repo.add(carte1)
        new_carte = Carte('1', 'eee', 'ffff', 'ggg')
        self._carti_repo.update(new_carte)
        self.assertEqual(self._carti_repo.get_by_id('1').get_titlu_carte(), "eee")
        self.assertEqual(self._carti_repo.get_by_id('1').get_descriere_carte(), "ffff")

    def test_delete(self):
        carte1 = Carte('1', 'aaa', 'bbb', 'Lvvvcc')
        carte2 = Carte('2', 'bbb', 'eee', 'sddd')
        self._carti_repo.add(carte1)
        self._carti_repo.add(carte2)
        self.assertEqual(self._carti_repo.__len__(), 2)
        self._carti_repo.delete('2')
        self.assertEqual(self._carti_repo.__len__(), 1)
        self.assertEqual(self._carti_repo.get_by_id('2'), None)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class ClientRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._clienti_repo = ClientRepository()

    def test_add(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        self.assertEqual(self._clienti_repo.__len__(), 0)
        self._clienti_repo.add(client1)
        self.assertEqual(self._clienti_repo.__len__(), 1)

    def test_get_clienti(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        client2 = Client('2', 'Alex', '5220309011234')
        clienti = {
            '1': client1,
            '2': client2
        }
        self._clienti_repo.add(client1)
        self._clienti_repo.add(client2)
        self.assertEqual(self._clienti_repo.get_clienti(), clienti)

    def test_set_clienti(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        client2 = Client('2', 'Alex', '5220309011234')
        self._clienti_repo.add(client1)
        self._clienti_repo.add(client2)
        client3 = Client('3', 'Munteanu Adrian', '5220324015964')
        client4 = Client('4', 'Neamt Victor', '5220526015748')
        clienti = {
            3: client3,
            4: client4
        }
        self._clienti_repo.set_clienti(clienti)
        self.assertEqual(self._clienti_repo.get_clienti(), clienti)

    def test_get_by_id(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        self._clienti_repo.add(client1)
        self.assertEqual(self._clienti_repo.get_by_id('1').get_id_client(), '1')

    def test_get_by_nume(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        self._clienti_repo.add(client1)
        self.assertEqual(self._clienti_repo.get_by_id('1').get_nume_client(), 'Ion Popa')

    def test_get_by_cnp(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        self._clienti_repo.add(client1)
        self.assertEqual(self._clienti_repo.get_by_id('1').get_cnp_client(), '5220309019075')

    def test_find(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        self._clienti_repo.add(client1)
        self.assertEqual(self._clienti_repo.get_by_id('1'), client1)
        self.assertEqual(self._clienti_repo.get_by_id('2'), None)

    def test_get_all(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        self._clienti_repo.add(client1)
        self.assertEqual(len(self._clienti_repo.get_all()), 1)

    def test_update(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        self._clienti_repo.add(client1)
        new_client = Client('1', 'Alex', '5220309011234')
        self._clienti_repo.update(new_client)
        self.assertEqual(self._clienti_repo.get_by_id('1').get_nume_client(), "Alex")
        self.assertEqual(self._clienti_repo.get_by_id('1').get_cnp_client(), "5220309011234")

    def test_delete(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        client2 = Client('2', 'Alex', '5220309011234')
        self._clienti_repo.add(client1)
        self._clienti_repo.add(client2)
        self.assertEqual(self._clienti_repo.__len__(), 2)
        self._clienti_repo.delete('2')
        self.assertEqual(self._clienti_repo.__len__(), 1)
        self.assertEqual(self._clienti_repo.get_by_id('2'), None)

    def test_clear_clienti(self):
        client1 = Client('1', 'Ion Popa', '5220309019075')
        client2 = Client('2', 'Alex', '5220309011234')
        self._clienti_repo.add(client1)
        self._clienti_repo.add(client2)
        self._clienti_repo.clear_clienti()
        self.assertEqual(self._clienti_repo.__len__(), 0)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class InchiriereRepositoryTest(unittest.TestCase):
    def setUp(self) -> None:
        self._carti_repo = CarteFileRepository('carte.txt')
        self._clienti_repo = ClientFileRepository('client.txt')
        self._inchiriere_repo = InchiriereRepository(self._clienti_repo, self._carti_repo)

    def test_add(self):
        clear_file('carte.txt')
        carte1 = Carte('3', 'aaa', 'bbb', 'ccc')

        self._carti_repo.add(carte1)
        clear_file('client.txt')

        client1 = Client('3', 'Ion Popa', '5220309019075')
        self._clienti_repo.add(client1)

        inchiriere1 = Inchiriere('3', '3', '3')
        self.assertEqual(self._inchiriere_repo.__len__(), 0)
        self._inchiriere_repo.adauga(inchiriere1)
        self.assertEqual(self._inchiriere_repo.__len__(), 1)
        clear_file('carte.txt')
        clear_file('client.txt')

    def test_gaseste_inchiriere_dupa_id(self):
        clear_file('carte.txt')
        carte1 = Carte('2', 'aaa', 'bbb', 'ccc')
        self._carti_repo.add(carte1)
        clear_file('client.txt')
        client1 = Client('2', 'Ion Popa', '5220309019075')

        self._clienti_repo.add(client1)

        inchiriere1 = Inchiriere('2', '2', '2')
        self._inchiriere_repo.adauga(inchiriere1)
        self.assertEqual(self._inchiriere_repo.gaseste_inchiriere_dupa_id('2'), 0)

    def test_get_all(self):
        clear_file('carte.txt')
        carte1 = Carte('4', 'aaa', 'bbb', 'ccc')
        clear_file('carte.txt')
        self._carti_repo.add(carte1)
        clear_file('carte.txt')
        clear_file('client.txt')
        client1 = Client('6', 'Ion Popa', '5220309019075')
        clear_file('carte.txt')
        self._clienti_repo.add(client1)
        clear_file('carte.txt')
        inchiriere1 = Inchiriere('5', '6', '4')

        self._inchiriere_repo.adauga(inchiriere1)
        self.assertEqual(len(self._inchiriere_repo.get_all()), 1)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class CarteServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._carti_repo = CarteFileRepository('cartesrv.txt')
        self._carte_validator = CarteValidator()
        self._carte_service = CarteService(self._carti_repo, self._carte_validator)

    def test_add(self):
        self._carte_service.add_carte('10', 'aaa', 'bbb', 'ccc')
        self._carte_service.add_carte('11', 'dddd', 'www', 'ccc')
        self.assertEqual(len(self._carte_service.get_all_carti()), 3)
        carti = self._carte_service.get_all_carti()
        assert carti[0].get_titlu_carte() == 'aaa'
        assert carti[0].get_descriere_carte() == 'bbb'
        assert carti[1].get_titlu_carte() == 'dddd'
        assert carti[1].get_descriere_carte() == 'www'

    def test_update(self):
        self._carte_service.update_carte('10', 'ion', 'roman', 'lv')
        carti = self._carte_service.get_all_carti()
        assert carti[0].get_titlu_carte() == 'ion'
        assert carti[0].get_descriere_carte() == 'roman'

    def test_delete(self):
        self._carte_service.add_carte('15', 'aaa', 'bbb', 'ccc')
        self._carte_service.delete_carte('15')
        self.assertEqual(len(self._carte_service.get_all_carti()), 3)

    def test_get_all_carte(self):
        self.assertEqual(len(self._carte_service.get_all_carti()), 3)

    def tearDown(self):
        unittest.TestCase.tearDown(self)


class ClientServiceTest(unittest.TestCase):
    def setUp(self) -> None:
        self._client_repo = ClientFileRepository('clientsrv.txt')
        self._client_service = ClientService(self._client_repo)

    def test_add(self):
        self._client_service.add_client('5', 'aaa', '5220309019075')
        self._client_service.add_client('6', 'bbb', '5220309011234')
        self.assertEqual(len(self._client_service.get_all_clienti()), 2)
        clienti = self._client_service.get_all_clienti()
        assert clienti[0].get_nume_client() == 'aaa'
        assert clienti[0].get_cnp_client() == '5220309019075'
        assert clienti[1].get_nume_client() == 'bbb'
        assert clienti[1].get_cnp_client() == '5220309011234'

    def test_update(self):
        self._client_service.update_client('5', 'eeeee', '5220309010000')
        clienti = self._client_service.get_all_clienti()
        assert clienti[0].get_nume_client() == 'eeeee'
        assert clienti[0].get_cnp_client() == '5220309010000'

    def test_delete(self):
        self._client_service.add_client('8', 'jjjjjjjjj', '5220309011111')
        self._client_service.delete_client('8')
        self.assertEqual(len(self._client_service.get_all_clienti()), 2)

    def test_get_all_clienti(self):
        self.assertEqual(len(self._client_service.get_all_clienti()), 2)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

# def test_str(self):
#     self.assertTrue(self.carte.__str__() == "Id-ul cartii: " + str(
#         self.carte.get_id_carte()) + ":\ntitlul cartii: " + self.carte.get_titlu_carte() + "\ndescrierea cartii: " + self.carte.get_descriere_carte() + "\nautorul cartii: " + self.carte.get_autor_carte() + "\n")

# def test_str(self):
#     self.assertTrue(self.client.__str__() == "Id-ul clientului: " + str(
#         self.client.get_id_client()) + ":\nnumele clientului: " + self.client.get_nume_client() + "\nCNP-ul clientului: " + self.client.get_cnp_client() + "\n")

# def test_str(self):
#     self.assertTrue(self.inchiriere.__str__() == "Inchiriere: " + str(
#         self.inchiriere.get_id_inchiriere()) + ":\nID Client: " + self.inchiriere.get_client_id() + "\nID Carte: " + self.inchiriere.get_carte_id() + "\n")
# clear_file('client.txt')
# clear_file('carte.txt')
# carte1 = Carte('1', 'aaa', 'bbb', 'ccc')
# self._carti_repo.add(carte1)
#
# client1 = Client('1', 'Ion Popa', '5220309019075')
# self._clienti_repo.add(client1)
