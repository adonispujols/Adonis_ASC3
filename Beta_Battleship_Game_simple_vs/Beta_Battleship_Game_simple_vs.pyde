#Beta Battleship Game
#TRY USING FOR LOOPS
#REMOVE HARDCODING/ADD MORE VARIABLES
from random import *
grid = []
side =50            #side length of sqaure
boatCoord= [int(randrange(500)/side)*side,int(randrange(500)/side)*side]    #forces boat coordinates [x,y] to grid 
turn = 3            #maximum turns for player
queue = []          #to store graphics from hits and misses
result = 0          #0 for misses, 1 for hits
for i in range(10):          #creating board (range(rows) and append(coloumns))
        grid.append(["0"]*10)
def setup():
    size(500,500)
    print("Guess which tile the boat is in!")
    noLoop()
def draw():
    global grid
    global side
    global mouse_gridXCoord    #grid X coordinate of mouse (top left corner X coord)
    global mouse_gridYCoord    #grid Y coordinate of mouse (top left corner Y coord)
    global boatCoord
    global turn
    global queue
    global result
look above! took grid creation out of loop (not needed here)
    for i in range(len(grid)):         #for each row in grid
        for y in range (len(grid[i])):         #for each tile in each row
            fill(0,0,255)
            rect(i*side, y*side,side,side)         #tile
    print (boatCoord)
    if mouseButton==LEFT:
        mouse_gridXCoord = int(mouseX/side)*side
        mouse_gridYCoord = int(mouseY/side)*side  
        # if mouse_gridXCoord+.5*side)==queue[turn][0] and mouse_gridYCoord+.5*side)==queue[i][1]: #checking rectangle's coordinates against those stored in queue. If both the X and Y match an object's x,y stored in the list, the click will be null
        # print("You've already selected that tile! Please choose again.")
        if mouse_gridXCoord==boatCoord[0] and mouse_gridYCoord==boatCoord[1]:    #checks if point is in same grid as the boat    
            fill(255,0,0)
            ellipse(mouse_gridXCoord+.5*side,mouse_gridYCoord+.5*side, side,side)    #draws ellipse (.5*size places center coord to center of sqaure
            print("Direct Hit! You win!")
            result = 1
            #thing is defined at the top right corner of fith box in fifth row:
                #if your mouse clicks in any square whose corner has x<boat and y<boat
                #This is what always happned! The only reason you didn't realize it is because the coord kept changing!
             # why not push boatCoord and mouseCoord to corner of box?
        else:
            fill(255)
            ellipse(mouse_gridXCoord+.5*side,mouse_gridYCoord+.5*side, side,side)         #mouseX/100 creates a float (i.e. 2.5), then int()rounds that number down (2), and *100 creates the proper coordinates (200) 
            print("You Missed! You have "+str(turn)+" turn(s) left!")
            result = 0
        turn -= 1
        queue.append([mouse_gridXCoord+.5*side,mouse_gridYCoord+.5*side,result])    #stores tile graphic for next frame
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
     #Don't make red circles outside of ship range DONE
     #Make more than 1 tile ship
         #write a script so user knows the ship is down
     #Add different sizes of ships
     ####################
     #allow user to set ships o nthe grid
     #some sort of ai

    #Everything that a legitmate battleship game should have:


            