#Turtle is used to draw graphics on the screen
from turtle import Screen, Turtle

trt=Turtle()
trt.shape("turtle")
trt.color("red")

#Create a square
for _ in range(4):
    trt.forward(100)
    trt.left(90)





screen=Screen()
screen.exitonclick()