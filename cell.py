class cell:
    def __init__(self, x, y, alive, neighbors=None):
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

    def updateCell(self):
        total = 0
        for i in self.neighbors:
            print(i, end=",")
            if str(i) == 'x':
                total += 1
        print(" : " + str(total))

        if total < 2 and self.alive:
            self.alive = False
        elif total > 3 and self.alive:
            self.alive = False
        elif total == 3 and not self.alive:
            self.alive = True

