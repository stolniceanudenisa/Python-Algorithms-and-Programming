class Studenti:
    def __init__(self, id, nume, prezente, nota):
        self.id = id
        self.nume = nume
        self.prezente = prezente
        self.nota = nota

    def get_id(self):
        return self.id

    def get_prezenta(self):
        return self.prezente

    def get_prezenta(self):
        return self.nota

    def set_nota(self, nota):
        self.nota = nota


    def __str__(self):
        print("ID: " + str(self.id) + "\n" + "NUME: " + str(self.nume) + "\n" + "PREZENTE: " + str(self.prezente) + "\n" + "NOTA: " + str(self.nota) )