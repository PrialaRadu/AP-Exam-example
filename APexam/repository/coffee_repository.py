from domain.entities import Coffee
from domain.validators import CoffeeException


class RepositoryException(CoffeeException):
    pass


class CoffeeRepository:
    def __init__(self, coffee_validator, file_name="data/coffees_txt"):
        self.__coffee_validator = coffee_validator
        self.__file_name = file_name
        self.__coffees = self.load_data()

    def save(self, coffee):
        self.__coffee_validator.validate(coffee)

        if coffee.idc in self.__coffees.keys():
            raise RepositoryException(f"id = {coffee.idc} already exists")

        names = [cof.name for cof in self.__coffees.values()]
        if coffee.name in names:
            raise RepositoryException(f"name = {coffee.name} already exists")

        with open(self.__file_name, 'a') as f:
            f.write(f"\n{coffee.idc},{coffee.name},{coffee.country},{coffee.price}")

        self.__coffees[coffee.idc] = coffee

    def load_data(self):
        coffees = {}
        with open(self.__file_name, 'r') as f:
            for line in f:
                arr = line.strip().split(',')
                coffee = Coffee(int(arr[0]), arr[1], arr[2], float(arr[3]))

                self.__coffee_validator.validate(coffee)
                coffees[coffee.idc] = coffee
        return coffees

    def find_all(self):
        return self.__coffees.values()
