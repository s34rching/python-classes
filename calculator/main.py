from ascii_art import logo
import os

operations_message = "+\n-\n*\n/"


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(number, s_number, operation):
    function = operations[operation]

    return function(number, s_number)

def calculator():
    intermediate_result = 0
    is_proceed_with_result = True

    os.system("clear")
    print(logo)
    first_number_input = input("What's is the first number?: ")
    initial_number = float(first_number_input)

    while is_proceed_with_result:
        print(operations_message)
        operation_input = input("Pick an operation: ")
        second_number_input = input("What's is the second number?: ")
        second_number = float(second_number_input)

        intermediate_result = calculate(initial_number, second_number, operation_input)

        print(f"{first_number_input} {operation_input} {second_number_input} = {intermediate_result}")

        proceed_with_result = input(f"Type 'y' to continue with {intermediate_result}, or type 'n' to start a new calculation: ")

        if (proceed_with_result == 'y'):
            first_number_input = f"{intermediate_result}"
            initial_number = intermediate_result
        elif (proceed_with_result == 'n'):
            calculator()
        else:
            print('Calculation is finished')
            break


calculator()
