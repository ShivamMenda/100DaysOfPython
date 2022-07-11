
# #turtle
# from turtle import Turtle,Screen
# test=Turtle()
# test.shape("turtle")
# test.color("red")
# test.forward(100.0)
# my_screen= Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

#Using Pretty table class
from prettytable import PrettyTable

table = PrettyTable() #Create a new object for class PrettyTable
table.field_names = ["Pokemon name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander","Fire"],
    ]
)
print(table)
