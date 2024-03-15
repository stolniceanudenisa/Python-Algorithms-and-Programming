from domeniu.exceptii.ValidationError import ValidationError
from domeniu.training import Training


class TrainingValidator:
    def valideaza(self, training: Training):
        erori = []
        if len(training.getNume()) > 20:
            erori.append("Numele nu poate fi mai lung de 20!")
        if training.getDurata() <= 0:
            erori.append("Durata trainingului trebuie sa fie un nr. strict pozitiv!")
        if len(erori) > 0:
            raise ValidationError(erori)