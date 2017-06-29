from turtle import *
import math

# Name your Turtle.
#t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
another = True

jess = Turtle()
jess.turtlesize(2,2)
jess.pensize(5)
jess.pendown()


while another == True:
    print("How many sides do you want your shape to have?")
    numSides = int(input())
    
    print ("What color do you wnat your shape to be?")
    chosenColor = input()
    
    drawShape(jess,numSides,chosenColor)
    
    print ("Do you wnat to draw another shape?")
    answer = input()
    
    if (answer =="no"):
    another = False 

    

print("All done")




# Close window on click.
exitonclick()
