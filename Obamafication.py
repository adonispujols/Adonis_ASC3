##Simple code that turns any pic into an "Obama/Hope" picture.
from Myro import *
##Defines the four standard colors used for Obama posters
darkblue = makeColor(0,51,76)
ObamaRed = makeColor(217,26,33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)
##Adds picture to memory
pic = makePicture(pickAFile())
##Changes each pixel to a color defined above based off of gray value
#Grayvalue is a measure of how "dark/light" the pixel is
for pixel in getPixels(pic):
    gray=getGray(pixel)
    if gray>180:
        setColor(pixel, ObamaYellow)
    elif gray>140:
        setColor(pixel, ObamaBlue)
    elif gray>80:
      setColor(pixel, ObamaRed)
    else:
      setColor(pixel, darkblue)
show(pic)