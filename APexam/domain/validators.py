class CoffeeException(Exception):
    pass


class ValidatorException(CoffeeException):
    pass


class CoffeeValidator:
    @staticmethod
    def validate(coffee):
        if len(coffee.name) < 3 or coffee.name[0].islower():
            raise ValidatorException(f"name = {coffee.name} should contain 3+ chars and should start with uppercase")
        if coffee.price <= 0:
            raise ValidatorException(f"price = {coffee.price} should be greater than 0")
