#USE FOR LOOPS INSTEAD OF TONS OF TESTS!!
#Our own ms-paint app that uses 8 clickable sqaures that change the color of our strokes
#USE COLORMODE()
draw_color = color(0,0,0)
r = 0
g = 0
b = 0
def setup():
    size(400,400)
    background(255)
def draw():
    global draw_color
    global r
    global g
    global b
    ## the eight squares
    noStroke()
    fill(255,0,0)
    rect(0,0,50,50)
    fill(0,255,0)
    rect(50,0,50,50)
    fill(0,0,255)
    rect(100,0,50,50)
    fill(100,100,0)
    rect(150,0,50,50)
    fill(0,200,50)
    rect(200,0,50,50)
    fill(50,150,200)
    rect(250,0,50,50)
    fill(255,255,255)
    rect(300,0,50,50)
    fill(0,0,0)
    rect(350,0,50,50)
    ##making them clicakable/changing colors
    if mouseButton == LEFT:
        if mouseY<50:    
            if 0 < mouseX < 50:
                draw_color = color(255,0,0)
            elif 50 < mouseX < 100:
                draw_color = color(0,255,0)
            elif 100 < mouseX < 150:
                draw_color = color(0,0,255)
            elif 150 < mouseX < 200:
                draw_color = color(100,100,0)
            elif 200 < mouseX < 250:
                draw_color = color(0,200,50)
            elif 250 < mouseX < 300:
                draw_color = color(50,150,200)
            elif 300 < mouseX < 350:
                draw_color = color(255,255,255)
            elif 350 < mouseX < 400:
                draw_color = color(0,0,0)  
        else:
            noStroke()                #drawing the stroke
            fill(draw_color)
            ellipse(mouseX,mouseY,5,5)
#REPLACE IFS WITH FOR LOOPS! ADD RAINBOW GRADIENT/ COLORING!
#use COLoRMODE()
                