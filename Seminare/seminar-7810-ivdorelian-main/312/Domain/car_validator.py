from Domain.car import Car

class CarValidationError(Exception):
    pass

class CarValidator:

    def validate(self, car: Car):
        valid_comforts = ['standard', 'ridicat', 'premium']
        if car.comfort_level not in valid_comforts:
            raise CarValidationError('Nivelul de comfort trebuie'
                             f'sa fie unul dintre {valid_comforts}')