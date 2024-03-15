class TrainingRepository:
    def __init__(self):
        self.__traininguri = {}

    def getAll(self):
        return list(self.__traininguri.values())

    def getById(self, idTraining):
        if idTraining in self.__traininguri:
            return self.__traininguri[idTraining]
        return None

    def adauga(self, training):
        if self.getById(training.getIdTraining()) is not None:
            raise KeyError("Exista deja un training cu id-ul dat!")
        self.__traininguri[training.getIdTraining()] = training

    def modifica(self, trainingNou):
        if self.getById(trainingNou.getIdTraining()) is None:
            raise KeyError("Nu exista niciun training cu id-ul dat!")
        self.__traininguri[trainingNou.getIdTraining()] = trainingNou

    def sterge(self, idTraining):
        if self.getById(idTraining) is None:
            raise KeyError("Nu exista niciun training cu id-ul dat!")
        self.__traininguri.pop(idTraining)
