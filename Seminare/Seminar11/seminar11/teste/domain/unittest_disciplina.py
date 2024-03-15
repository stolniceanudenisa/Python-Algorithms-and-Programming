from unittest import TestCase
import unittest

class TestEntitate(TestCase):
    def setUp(self):
        from seminar11.clase.domain.Entitate import Entitate
        self.entitate = Entitate(1)

    def test_id(self):
        self.assertTrue(self.entitate.get_id() == 1)

class TestDisciplina(TestCase):
    def setUp(self):  #metoda setUp este ca o initializare, executata INAINTE de fiecare test
        from seminar11.clase.domain.Disciplina import Disciplina
        self.disciplina = Disciplina(101, "AP-22", "Radu Gaceanu")

    def test_id(self):
        self.assertTrue(self.disciplina.get_id() == 101, "Id-ul disciplinei trebuie sa fie 101!")
        self.disciplina.set_id(102)
        self.assertTrue(self.disciplina.get_id() == 102, "Id-ul disciplinei trebuie sa fie 102!")

    def test_nume(self):
        self.assertTrue(self.disciplina.get_nume() == "AP-22", "Numele disciplinei trebuie sa fie AP-22!")
        self.disciplina.set_nume("AP-23")
        self.assertTrue(self.disciplina.get_nume() == "AP-23")

    def test_profesor(self):
        self.assertTrue(self.disciplina.get_profesor() == "Radu Gaceanu", "Numele profesorului trebuie sa fie Radu Gaceanu!")
        self.disciplina.set_profesor("Sara")
        self.assertTrue(self.disciplina.get_profesor() == "Sara")

    def test_str(self):
        self.assertTrue(self.disciplina.__str__() == "Disciplina " + str(self.disciplina.get_id()) + ":\nNume: " + self.disciplina.get_nume() + "\nProfesor: " + self.disciplina.get_profesor() + "\n")

    def tearDown(self) -> None: #metoda se executa DUPA fiecare test
        pass
