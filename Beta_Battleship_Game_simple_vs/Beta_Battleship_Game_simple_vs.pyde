#Beta Battleship Game
#TRY USING FOR LOOPS
#REMOVE HARDCODING/ADD MORE VARIABLES
from random import *
grid = []
side =50            #side length of sqaure
boatCoord= [150,150]    #boat coordinates [x,y]) 
turn = 3            #maximum turns for player
queue = []          #to store graphics from hits and misses
result = 0          #0 for misses, 1 for hits
def setup():
    size(500,500)
    print("Guess which tile the boat is in!")
    noLoop()
def draw():
    global grid
    global side
    global boatCoord
    global turn
    global queue
    global result
    for i in range(10):          #creating board (range(rows) and append(coloumns))
        grid.append(["0"]*10)
    for i in range(len(grid)):         #for each row in grid
        for y in range (len(grid[i])):         #for each tile in each row
            fill(0,0,255)
            rect(i*side, y*side,side,side)         #tile
    # for i in range(2):              #creates x and y coordinates for boat
    #     boatCoord[i] = randrange(1000)       #getting random x,y coord for boat
    print (boatCoord)
    if mouseButton==LEFT:
        # if int(mouseX/side)*side+.5*side)==queue[i][0] and int(mouseY/side)*side+.5*side)==queue[i][1]: #checking rectangle's coordinates against those stored in queue. If both the X and Y match an object's x,y stored in the list, the click will be null
        # print("You've already selected that tile! Please choose again.")
        if int(mouseX/side)*side+.5*side<boatCoord[0] and int(mouseY/side)*side+.5*side<boatCoord[1]:        
            fill(255,0,0)
            ellipse(int(mouseX/side)*side+.5*side,int(mouseY/side)*side+.5*side, side,side)
            print("Direct Hit! You win!")
            result = 1
        else:
            fill(255)
            ellipse(int(mouseX/side)*side+.5*side,int(mouseY/side)*side+.5*side, side,side)         #mouseX/100 creates a float (i.e. 2.5), then int()rounds that number down (2), and *100 creates the proper coordinates (200) 
            print("You Missed! You have "+str(turn)+" turn(s) left!")
            result = 0
        turn -= 1
        queue.append([int(mouseX/side)*side+.5*side,int(mouseY/side)*side+.5*side,result])    #stores tile graphic for next frame
    if turn<1:
        print("GAVE OVER Try again!")
        turn = 3
    for i in range(len(queue)):                    #redraw stored objects with proper color/position
        if queue[i][2]==1:
            fill(255,0,0)
            ellipse(queue[i][0],queue[i][1],side,side)
        else:
            fill(255)
            ellipse(queue[i][0],queue[i][1],side,side)
def mousePressed():
    redraw()    #forces our tile image to appear
###LAST FEATURE BEFORE PIMPING:
     #Must make "you win" screen last longer befoer exit
  ###LAST FEATURE BEFORE PIMPING:
     #Give out an error when same tile is selected again
     #only create the ships once DONE
     #Don't make red circles outside of ship range
     #Make more than 1 tile ship
         #write a script so user knows the ship is down
     #Add different sizes of ships
     ####################
     #allow user to set ships o nthe grid
     #some sort of ai

    #Everything that a legitmate battleship game should have:
        #FIX DOUBLE OBJECT CREAITON BUG


            