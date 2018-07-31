from immagini import *

class Robot(object):

    def __init__(self, cellsN, size, field, colors):
        self.position = [0,0]
        self.direction = 0
        self.shifts = 0
        self.limit = cellsN * size
        self.size = size
        self.field = field
        self.colors = colors
        self.steps = ''
        self.obstImg = [[colors['obst']] * self.size] * self.size
        self.stpdImg = [[colors['stpd']] * self.size] * self.size
    
    def getCell(self, i, j):
        return [row[j:j+self.size] for row in self.field[i:i+self.size]]
    
    def rotate(self):
        self.direction = (self.direction + 1) % 4
        self.shifts += 1
    
    def colorCurrentCell(self, cType):
        color = self.colors[cType]
        for i in range(self.position[0], self.position[0] + self.size):
            for j in range(self.position[1], self.position[1] + self.size):
                self.field[i][j] = color
    
    def isAvailable(self, cell):
        return cell != self.obstImg and cell != self.stpdImg
    
    def forward(self):
        moved = False
        if self.direction == 0:
            if self.position[1] + self.size < self.limit:
                nextC = self.getCell(self.position[0], self.position[1]+self.size)
                if self.isAvailable(nextC):
                    self.position[1] += self.size
                    self.shifts = 0
                    self.steps += str(self.direction)
                    moved = True
        elif self.direction == 1:
            if self.position[0] + self.size < self.limit:
                nextC = self.getCell(self.position[0]+self.size, self.position[1])
                if self.isAvailable(nextC):
                    self.position[0] += self.size
                    self.shifts = 0
                    self.steps += str(self.direction)
                    moved = True
        elif self.direction == 2:
            if self.position[1] - self.size >= 0:
                nextC = self.getCell(self.position[0], self.position[1]-self.size)
                if self.isAvailable(nextC):
                    self.position[1] -= self.size
                    self.shifts = 0
                    self.steps += str(self.direction)
                    moved = True
        else:
            if self.position[0] - self.size >= 0:
                nextC = self.getCell(self.position[0]-self.size, self.position[1])
                if self.isAvailable(nextC):
                    self.position[0] -= self.size
                    self.shifts = 0
                    self.steps += str(self.direction)
                    moved = True
        return moved
        

def cammino(fname,  fname1):
    img = load(fname)
    
    colors = {'obst':(255,0,0),'stpd':(0,255,0),'stop':(0,0,255)}
    
    robot = Robot(15, 40, img, colors)
    
    notStopped = True
    moved = True
    
    
    while notStopped:
        if moved:
            robot.colorCurrentCell('stpd')
        
        moved = robot.forward()
        if not moved:
            robot.rotate()
            if robot.shifts == 4:
                robot.colorCurrentCell('stop')
                notStopped = False
        
    
    save(robot.field, fname1)
    
    return robot.steps