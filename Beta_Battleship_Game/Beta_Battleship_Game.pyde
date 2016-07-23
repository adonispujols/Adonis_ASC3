#Beta Battleship Game
grid = []
# grid.insert(
side=100
def setup():
    size(500,500)
    noLoop()
def draw():
    global grid
    global side
    for i in range(5):          #creating board (range(rows) and append(coloumns))
        grid.append(["0"]*5)
    for i in range(len(grid)):
        for y in range (len(grid[i])):
            fill(0,0,255)
            rect(i*side, y*side,side,side)
            grid[i].insert(y,[[i*side,i*side+side],[y*side,y*side+side]])   #grid[column][row]
            print(grid[0][0])
            
# if box grid[0][0][0][0]<mouseX<grid[0][0][0][1] and grid[0][0][1][0]<mouseY<box[1][1]:
    
#     grid[column][row] 
#                       tile = [column[row[x1,x2],[y1,y2]]]