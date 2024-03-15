#  indicativ, nivel confort (standard, ridicat, premium), plata cu cardul (da / nu), model.
from domain.ValidationException import ValidationException


class CarValidator:
    def validate(self, car):
        errors = []
        if car.plata_card == 'da':
            car.plata_card = True
        elif car.plata_card == 'nu':
            car.plata_card = False
        try:
            car.id = int(car.id)
        except:
            errors.append('Idul trebuie sa fie int')
        try:
            car.indicativ = int(car.indicativ)
        except:
            errors.append('Indicativul trebuie sa fie int')
        if car.confort not in ['standard', 'high', 'premium']:
            errors.append('Confortul trebuie sa fie unul dintre: standard, high, premium!')
        if car.plata_card not in [True, False]:
            errors.append('Plata cu cardul trebuie sa fie una dintre: da, nu')
        if errors != []:
            raise ValidationException(errors)


