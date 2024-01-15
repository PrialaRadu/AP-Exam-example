class Coffee:
    def __init__(self, idc, name, country, price):
        self.__idc = idc
        self.__name = name
        self.__country = country
        self.__price = price

    def __str__(self):
        return f"id = {self.__idc}, name = {self.__name}, country = {self.__country}, price = {self.__price}"

    @property
    def idc(self):
        return self.__idc

    @property
    def name(self):
        return self.__name

    @property
    def country(self):
        return self.__country

    @property
    def price(self):
        return self.__price
