# Calculator

# Add
from replit import clear

from art import logo

import pyfiglet

import os

os.system('clear')
print(logo)


def add(n1, n2):
    return n1 + n2


# Subtract

def subtract(n1, n2):
    return n1 - n2


# Multiply

def multiply(n1, n2):
    return n1 * n2


# Divide

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("enter the first number : "))
    should_continue = True
    for symbols in operations:
        print(symbols)

    while should_continue:

        operation_symbol = input("choose an operation: ")
        print("\n")
        print("You chose : ")
        print(pyfiglet.figlet_format(operation_symbol))

        num2 = float(input("whats the next number : "))
        print("\n")

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}\n")
        print("\n")

        if input(
                f"type 'y' to continue working with {answer},  or type 'n' to start a new calculation  or type 'exit' "
                f"to close the applicaton: \n") == "y":
            num1 = answer

        if input(
                f"type 'y' to continue working with {answer},  or type 'n' to start a new calculation  or type 'exit' "
                f"to close the applicaton: \n") == "n":
            should_continue = False
            clear()
            os.system('clear')
            print(logo)
            calculator()

        if input(
                f"type 'y' to continue working with {answer},  or type 'n' to start a new calculation  or type 'exit' "
                f"to close the applicaton: \n") == "exit":
            clear()
            os.system('clear')
            exit()


calculator()
