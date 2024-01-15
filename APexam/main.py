from domain.validators import CoffeeValidator
from repository.coffee_repository import CoffeeRepository
from service.coffee_service import CoffeeService
from ui.console import CoffeeConsole

if __name__ == '__main__':
    coffee_validator = CoffeeValidator()
    coffee_repository = CoffeeRepository(coffee_validator)
    coffee_service = CoffeeService(coffee_repository)
    coffee_console = CoffeeConsole(coffee_service)

    coffee_console.run_console()
