# import turtle
#
# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(200)
# myscreen = turtle.Screen()
# myscreen.exitonclick()

# from prettytable import PrettyTable
#
# table = PrettyTable()
#
# table.field_names = ["Pokémon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
# table.align = "l"
# print(table)

from lib.menu import Menu, MenuItem
from lib.coffee_maker import CoffeeMaker
from lib.money_machine import MoneyMachine
import os


menu = Menu()

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True

while is_on:
    os.system('cls')
    order = input(f"What would you like? ({menu.get_items()})\n")
    if order == 'off':
        is_on = False
    elif order == 'report':
        coffee_maker.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)
        else:
            print("Not enough resources")
