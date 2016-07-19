##FINISH COLLISION DETECTOR FOR ALL OBJECTS (OR ENTIRE FACE)

xCoordinate_face = 100
yCoordinate_face = 120
xCoordinate_ear = xCoordinate_face-50
yCoordinate_ear = yCoordinate_face-60
width_face = 120
length_face = 120
width_ear = width_face*(.7)
length_ear = length_face*(.7)
def setup():
    size(400,400)
def draw():
    global xCoordinate_face
    global yCoordinate_face
    global xCoordinate_ear
    global yCoordinate_ear
    background(50)
    fill(0)
    ellipse(xCoordinate_ear, yCoordinate_ear, width_ear, length_ear)
    ellipse(xCoordinate_ear, yCoordinate_ear, width_ear, length_ear)
    fill(255)
    ellipse(xCoordinate_face, yCoordinate_face, width_face, length_face)
    xCoordinate_face += 1
    yCoordinate_face += 1
    xCoordinate_ear += 1
    yCoordinate_ear += 1
    if xCoordinate_ear>400-width_ear:
        xCoordinate_face -= 1
    if yCoordinate_face>400-length_ear:
        yCoordinate_face -= 1