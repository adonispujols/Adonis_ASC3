#Makes a ball bounce off the walls at set angles but starting from a random direction
from random import *
#Setting varaibles for easy customization
x_boundary = 400
y_boundary = 400
x_coordinate = 200
y_coordinate = 200
speed_x = randrange (1,5)        #both changes in x and y are randomized to make ball move in random direction
speed_y = randrange (1,5) 
def setup():
    global x_coordinate
    global y_coordinate
    size(x_boundary,y_boundary)
def draw():
    global x_coordinate
    global y_coordinate
    global speed_x
    global speed_y
    background(255)
    noStroke()
    fill(0)
    ellipse(x_coordinate,y_coordinate,50,50)
    ## Checks if ball collided with a wall, then changes its speed appropriately
    if 25>x_coordinate or x_coordinate>375:
        speed_x = speed_x*-1
    if 25>y_coordinate or y_coordinate>375:    
        speed_y = speed_y*-1
    x_coordinate +=speed_x
    y_coordinate +=speed_y
    print(x_coordinate, y_coordinate,collision_state)