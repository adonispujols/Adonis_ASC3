#Space Invaders! Early Beta Version
alienXcoord = 225
alienYcoord = 100
laserX = 240
laserY = 150
def setup():
    size(500,500)
def draw():
    global alienXcoord
    global alienYcoord
    global laserX
    global laserY
    fill(255,0,0)
    rect(alienXcoord,alienYcoord,50,50)        #alien (one for now)
    if alienXcoord<=laserX<=alienXcoord+50 and laserY==alienYcoord+50: #checks if laser is inbetween object and y coordinate of the bottom side (and thus "hit" it)
          fill(0)            #fills object area to background to create illusion of "destruction"
# Basic Plan:

# Make rectangle at bottom
#     Then Make rectangle move with keyboard press (use the paddle project) left and right only
# Make the shooting object
#     THEN, make it shoot with spacebar )from the box)
# Make the alien object
#     then make it dissapear when hit with object
#     have it move left the right
#     then make a row of these
    
    
# Variables:
# alienXcoord    x coordinate of alien 
# alienYcoord    y coordinate of alien 
# shipX          x coordinate of ship
# laserX         x coordinate of ship
# laserY         y coordinate of ship

# x=(500)   no need
# xspeed = 2     x speed of ship