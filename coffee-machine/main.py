from data import MENU, resources


def print_report(remaining_resources):
    print(f"Water: {remaining_resources['water']}ml")
    print(f"Milk: {remaining_resources['milk']}ml")
    print(f"Coffee: {remaining_resources['coffee']}g")
    print(f"Money: ${remaining_resources['money']}")


def get_missing_resources(desired_drink, remaining_resources):
    missing_resources = []

    for ingredient in desired_drink["ingredients"]:
        if remaining_resources[ingredient] < desired_drink["ingredients"][ingredient]:
            missing_resources.append(ingredient)

    return missing_resources


def get_missing_resources_message(missing_resources):
    missing = ", ".join(missing_resources)

    return f"Sorry, not enough resources: {missing}"


def request_payment():
    quarters_count = int(input("How many quarters?: "))
    dimes_count = int(input("How many dimes?: "))
    nickles_count = int(input("How many nickles?: "))
    pennies_count = int(input("How many pennies?: "))

    inserted_money = quarters_count * 0.25 + dimes_count * 0.1 + nickles_count * 0.05 + pennies_count * 0.01
    return inserted_money


def coffee_machine():
    current_resources = resources.copy()
    current_resources['money'] = 0

    def update_resources(drink):
        for ingredient in desired_drink["ingredients"]:
            current_resources[ingredient] -= drink["ingredients"][ingredient]
        current_resources["money"] += drink["cost"]

    is_machine_on = True
    while is_machine_on:
        customer_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if customer_input in MENU.keys():
            desired_drink = MENU[customer_input]

            missing_resources = get_missing_resources(desired_drink, current_resources)

            if len(missing_resources) == 0:
                print(f"The cost of {customer_input} is ${'{:.2f}'.format(desired_drink['cost'])}. Please insert your "
                      f"money.")
                inserted_money = request_payment()

                delta = inserted_money - desired_drink["cost"]

                if delta < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    if delta > 0:
                        print(f"Here is ${'{:.2f}'.format(delta)} dollars in change.")
                    print(f"Here is your {customer_input}. Enjoy your drink!")

                    update_resources(desired_drink)
            else:
                print(get_missing_resources_message(missing_resources))
        elif customer_input == "off":
            is_machine_on = False
        elif customer_input == "report":
            print_report(current_resources)
        else:
            print("Unknown drink...")


coffee_machine()
