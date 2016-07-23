#Makes a ball bounce off the walls at set angles but different speeds
#TOO MUCH HARDCODING! Add more varialbes (i.e. collision detection)
#Fix start/gameover screens!
     #TRY "redraw()" to correct!
from random import *
import time
#Setting varaibles for easy customization
gameStart = False
x_boundary = 400
y_boundary = 400
x_coordinate = 200
y_coordinate = 200
speed_x = randrange (1,5)        #both changes in x and y are randomized to make ball move in random direction
speed_y = randrange (1,5) 
counter = 0
def setup():
    size(x_boundary,y_boundary)
    noLoop()
def draw():
    global gameStart
    global x_coordinate
    global y_coordinate
    global speed_x
    global speed_y
    global counter
    if gameStart == False:
        background(0)
        textSize(40)
        text("Ping Pong Beta 0.1", 25, 100)
        textSize(32)
        text("Click to Start",100,150)
    else:
        background(255)
        textSize(25)
        text("Score:", 10, 30)
        text(counter, 90, 30)
        noStroke()
        fill(0,0,150)
        ellipse(x_coordinate,y_coordinate,50,50)                #the "ball"
        fill(0,0,150)
        rect(mouseX,350,100,10)
        #Collision detecting with ball (hit bounces, no hit should make it dissapear)
        if 25>x_coordinate or x_coordinate>375:
            speed_x = speed_x*-1
        if 25>y_coordinate or y_coordinate>325:    
            speed_y = speed_y*-1
        x_coordinate +=speed_x
        y_coordinate +=speed_y
        # Checks if ball collided with a wall, then changes its speed appropriately
        if y_coordinate>325 and mouseX<x_coordinate<mouseX+100:      #essentially mouseX + width
            counter += 1
        elif y_coordinate>325:
            # "Game Over" Screen displaying score
            background(150,0,0)
            textSize(40)
            fill(255)
            text("GAME OVER",100,150)
            text("Final Score:",50,200)
            text(counter,150,200)
def mousePressed():
    #TRY redraw()
    loop()
    gameStart == True
   
# Gameover/ Dissapear ball screen:
    #first need to make ball disppear (automatic restart--->have game wait a moment before continueing)
    #Add lifs
#Have ball change speed randomly at each bounce (but not direction)
#Graphics???
    #I.E> Raibow graphics?! (once we get gradient color change to work!)