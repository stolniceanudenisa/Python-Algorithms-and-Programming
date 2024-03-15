from Domain.car import Car


class CarValidator:
    def validate(self, car: Car):
        comforts = ['standard', 'ridicat', 'premium']
        if car.comfort_level not in comforts:
            raise ValueError(f'{car.comfort_level} nu e un nivel '
                             f'valid, valide sunt: {comforts}.')

