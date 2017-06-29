from turtle import *
import math


#setting up screen size
setup(500,500)

#functions
def whileDrawnShape(turtle,sides,color):
    turtle.pencolor(color)
    drawnSides = 0
    angle = 360/sides

    while drawnSides < sides:
        turtle.forward(50)
        turtle.rt(angle)
        drawnSides += 1
def forDrawnShape(turtle,sides,color):
  turtle.pencolor(color)
  angle = 360/sides

  for s in range(sides):
      turtle.forward(50)
      turtle.right(angle)
#printing Code
anah = Turtle()
anah.turtlesize(2,2)
anah.pensize(5)
anah.pendown()
another = True 
while another == True:
    print ("How many sides do you want your shape to have?/s")
    numSides = int(input())
    print ("What color do you wnat your shape to have?")
    chosenColor = input()
    forDrawnShape(anah,numSides,chosenColor)
    print("Do you wnat to draw another shape?")
    answer = input()
    if (answer == "no"):
            another = False
    if (answer == "yes"):
        anah.forward(90)
        anah.pendown()
    
#whileDrawnShape(anah,4,"green")
#anah.penup()
#anah.forward(100)
#anah.pendown()
#whileDrawnShape(anah,5,"pink")
#whileDrawnShape(diana,5,red)

#closes the turtle window on click 
