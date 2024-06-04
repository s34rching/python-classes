from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def order_coffee():
    machine_menu = Menu()
    money_handler = MoneyMachine()
    coffee_handler = CoffeeMaker()

    is_machine_on = True
    while is_machine_on:
        customer_input = input(f"What would you like? {machine_menu.get_items()}: ").lower()

        if customer_input == "report":
            coffee_handler.report()
            money_handler.report()
        elif customer_input == "off":
            is_machine_on = False
        else:
            desired_drink = machine_menu.find_drink(customer_input)

            if coffee_handler.is_resource_sufficient(desired_drink):
                if money_handler.make_payment(desired_drink.cost):
                    coffee_handler.make_coffee(desired_drink)


order_coffee()
