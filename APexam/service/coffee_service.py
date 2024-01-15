from domain.entities import Coffee


class CoffeeService:
    def __init__(self, coffee_repository):
        self.__coffee_repository = coffee_repository

    def add_coffee(self, idc, name, country, price):
        coffee = Coffee(idc, name, country, price)
        self.__coffee_repository.save(coffee)

    def get_all_coffees(self):
        return self.__coffee_repository.find_all()

    def get_coffees_by_country(self, country):
        return [cof for cof in self.__coffee_repository.find_all() if cof.country == country]

    def country_ranking(self):
        coffees = self.__coffee_repository.find_all()
        country_count = {}

        for cof in coffees:
            if cof.country in country_count.keys():
                country_count[cof.country] += 1
            else:
                country_count[cof.country] = 1

        sorted_dict = sorted(country_count.items(), key=lambda x: x[1], reverse=True)
        return sorted_dict[0][0]
