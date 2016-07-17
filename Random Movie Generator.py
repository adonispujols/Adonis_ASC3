## Create a random movie title from a set of words in lists
from Myro import *
from random import *
used_titles= []
##Defines three lists of words to create a title
subject = ["Revenge of ","Life of ", "How to Kill ","The Wonderful "]
adjective = ["Deadly ","Wombo ","Mongolian ","Alien "]
thing = ["Nanobots","Ghosts from Hell","Donald Trump","Who?"]
##Create a numbered list of ten random movie title
num = 0
while num<10:
    rs = randrange(len(subject))      #used to choose a random item within the list
    ra = randrange(len(adjective))
    rt = randrange(len(thing))
    title = subject[rs]+adjective[ra]+thing[rt]
    if title in used_titles:
        pass
    else:
        used_titles.append(title)
        num = num+ 1
        print(str(num)+". "+title)      
