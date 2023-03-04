#Coffee Machine in Object Oriented Programming (OOP)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()
machine_on = True

coffee_machine.report()
money_machine.report()

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == 'off':
        machine_on = False