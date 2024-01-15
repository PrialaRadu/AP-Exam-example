import traceback
from domain.validators import CoffeeException


class CoffeeConsole:
    def __init__(self, coffee_service):
        self.__coffee_service = coffee_service

    def __print_coffees(self):
        print(*self.__coffee_service.get_all_coffees(), sep='\n')

    def __add_coffee(self, idc, name, country, price):
        try:
            idc = int(idc)
            price = float(price)
            self.__coffee_service.add_coffee(idc, name, country, price)
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)

    def __print_coffees_by_country(self, country):
        print(*self.__coffee_service.get_coffees_by_country(country))

    def __country_ranking(self):
        return self.__coffee_service.country_ranking()

    def run_console(self):
        commands = self.__create_commands()
        while True:
            self.__print_commands(commands)
            try:
                cmd, args = self.__read_commands()
            except ValueError as ve:
                print(ve)
                continue
            except Exception as e:
                print(e)
                continue

            if cmd == 'exit':
                break

            old_win = self.__country_ranking()

            try:
                commands[cmd](*args)
            except CoffeeException as ce:
                print(ce)
                traceback.print_exc()
            except ValueError as ve:
                print(ve)
                traceback.print_exc()
            except KeyError as ke:
                print(ke)
                traceback.print_exc()
            except Exception as e:
                print(e)

            new_win = self.__country_ranking()

            if old_win != new_win:
                print(f"New Winner: {new_win}")

    @staticmethod
    def __help_commands(cmd):
        help_commands = {'add': 'Usage: add <idc>,<name>,<country>,<price>',
                         'print-all': 'Usage: print-all',
                         'print-by-country': 'print_by_country <country>',
                         'help': 'help <command>'}
        try:
            print(help_commands[cmd])
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def __create_commands(self):
        return {'add': self.__add_coffee,
                'print-all': self.__print_coffees,
                'print-by-country': self.__print_coffees_by_country,
                'help': self.__help_commands}

    @staticmethod
    def __print_commands(commands):
        print("Available commands: ")
        print(*commands.keys(), 'exit', sep=' --- ')
        print("For help, type: help <command>")

    @staticmethod
    def __read_commands():
        command = input("Command = ")
        pos = command.find(' ')

        if pos == -1:
            return command, []

        cmd = command[:pos]
        args = command[pos:]
        args = args.split(',')
        args = [s.strip() for s in args]

        return cmd, args
