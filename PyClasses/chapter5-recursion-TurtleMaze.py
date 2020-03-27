import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'


def searchFrom(maze, startRow, startColumn):
    maze.updatePosition(startRow, startColumn)
    # Check for base cases
    # 1. Obstacle, return false
    if maze[startRow][startColumn] == OBSTACLE:
        return False

    # 2. Found already explored square
    if maze[startRow][startColumn] == TRIED:
        return False

    # 3. Success, outside edge not Obstacle
    if maze.isExit(startRow, startColumn):
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
        return True

    maze.updatePosition(startRow, startColumn, TRIED)

    # Otherwise, use logical short circuiting to try each
    # direction in turn (if needed)
    found = searchFrom(maze, startRow-1, startColumn) or \
        searchFrom(maze, startRow+1, startColumn) or \
        searchFrom(maze, startRow, startColumn-1) or \
        searchFrom(maze, startRow, startColumn+1)
    print('found is', found)
    if found:
        maze.updatePosition(startRow, startColumn, PART_OF_PATH)
    else:
        maze.updatePosition(startRow, startColumn, DEAD_END)

    return found


mazeFile = '''
++++++++++++++++++++++\n
+   +   ++ ++     +   \n
+ +   +       +++ + ++\n
+ + +  ++  ++++   + ++\n
+++ ++++++    +++ +  +\n
+          ++  ++    +\n
+++++ ++++++   +++++ +\n
+     +   +++++++  + +\n
+ +++++++      S +   +\n
+                + +++\n
++++++++++++++++++ +++\n
'''


class Maze:
    def __init__(self, mazeFile):
        rowsInMaze = 0
        columnsInMaze = 0
        self.mazelist = []
        lines = mazeFile.split('\n')

        for line in lines:
            rowList = []
            col = 0
            for ch in line:
                rowList.append(ch)
                if ch == 'S':
                    self.startRow = rowsInMaze
                    self.startCol = col
                col += 1

            if rowList:
                self.mazelist.append(rowList)
                columnsInMaze = len(rowList)
                rowsInMaze += 1

        self.rowsInMaze = rowsInMaze
        self.columnsInMaze = columnsInMaze
        self.xTranslate = -columnsInMaze/2
        self.yTranslate = rowsInMaze/2
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.wn = turtle.Screen()
        self.wn.setup(400, 300)
        self.wn.setworldcoordinates(-(columnsInMaze-1)/2-.5, -(
            rowsInMaze-1)/2-.5, (columnsInMaze-1)/2+.5, (rowsInMaze-1)/2+.5)

    def drawMaze(self):
        self.t.speed(10)
        self.wn.tracer(0)
        for y in range(self.rowsInMaze):
            for x in range(self.columnsInMaze):
                if self.mazelist[y][x] == OBSTACLE:
                    self.drawCenteredBox(
                        x+self.xTranslate, -y+self.yTranslate, 'orange')
        self.t.color('black')
        self.t.fillcolor('blue')
        self.wn.update()
        self.wn.tracer(1)

    def drawCenteredBox(self, x, y, color):
        self.t.up()
        self.t.goto(x-.5, y-.5)
        self.t.color(color)
        self.t.fillcolor(color)
        self.t.setheading(90)
        self.t.down()
        self.t.begin_fill()
        for i in range(4):
            self.t.forward(1)
            self.t.right(90)
        self.t.end_fill()

    def moveTurtle(self, x, y):
        self.t.up()
        self.t.setheading(self.t.towards(
            x+self.xTranslate, -y+self.yTranslate))
        self.t.goto(x+self.xTranslate, -y+self.yTranslate)

    def dropBreadcrumb(self, color):
        self.t.dot(10, color)

    def updatePosition(self, row, col, val=None):
        if val:
            self.mazelist[row][col] = val
        self.moveTurtle(col, row)

        if val == PART_OF_PATH:
            color = 'green'
        elif val == OBSTACLE:
            color = 'red'
        elif val == TRIED:
            color = 'black'
        elif val == DEAD_END:
            color = 'red'
        else:
            color = None

        if color:
            self.dropBreadcrumb(color)

    def isExit(self, row, col):
        return (row == 0 or
                row == self.rowsInMaze-1 or
                col == 0 or
                col == self.columnsInMaze-1)

    def __getitem__(self, idx):
        return self.mazelist[idx]


myMaze = Maze(mazeFile)
print(myMaze.mazelist)
myMaze.drawMaze()
myMaze.updatePosition(myMaze.startRow, myMaze.startCol)

searchFrom(myMaze, myMaze.startRow, myMaze.startCol)
