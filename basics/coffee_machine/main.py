from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Requirements
#1.Print Report
c=CoffeeMaker()
c.report()
m=MoneyMachine()
m.report()

is_on=True


#2.Check Resources sufficient?
menu=Menu()
while is_on:
    options=menu.get_items()
    choice=input(f"What would you like? ({options}):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        c.report()
        m.report()
    else:
        drink=menu.find_drink(choice)
        if(c.is_resource_sufficient(drink)):
            #3. Process Transaction
            if(m.make_payment(drink.cost)):
                c.make_coffee(drink)

