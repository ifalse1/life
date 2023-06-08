class cell:
    def __init__(self, x, y, alive, neighbors=None):
        self.total = 0
        if neighbors is None:
            neighbors = []
        self.x = x
        self.y = y
        self.alive = alive
        self.neighbors = neighbors

    def __str__(self):
        if self.alive:
            return "x"
        else:
            return " "

    def getStatus(self):
        print("test")
        return self.alive

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def postNeighbors(self, neighbors):
        self.neighbors = neighbors

    def prepUpdateCell(self):
        self.total = 0
        for i in self.neighbors:
            if str(i) == 'x':
                self.total += 1

    def updateCell(self):
        if self.total < 2 and self.alive:
            self.alive = False
        elif self.total > 3 and self.alive:
            self.alive = False
        elif self.total == 3 and not self.alive:
            self.alive = True

