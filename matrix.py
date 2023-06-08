import random
from cell import cell


class matrix:
    def __init__(self, size):
        self.matrix = []
        self.size = size
        for i in range(size):
            self.matrix.append([])
            for j in range(size):
                if random.randint(1, 10) > 5:
                    self.matrix[i].append(cell(j, i, False))
                else:
                    self.matrix[i].append(cell(j, i, True))
        for i in range(self.size):
            for j in range(self.size):
                self.assignNeighbors(self.matrix[j][i])

    def assignNeighbors(self, cell):
        if cell.getX() == 0 and cell.getY() == 0:
            # Top Left Corner
            cell.postNeighbors(
                [self.matrix[cell.getY()][cell.getX() + 1], self.matrix[cell.getY() + 1][cell.getX() + 1],
                 self.matrix[cell.getY() + 1][cell.getX()]])
        elif cell.x == (self.size - 1) and cell.y == 0:
            # Top Right Corner
            cell.postNeighbors(
                [self.matrix[cell.getY()][cell.getX() - 1], self.matrix[cell.getY() + 1][cell.getX() - 1],
                 self.matrix[cell.getY() + 1][cell.getX()]])
        elif cell.x == 0 and cell.y == (self.size - 1):
            # Bottom Left Corner
            cell.postNeighbors(
                [self.matrix[cell.getY()][cell.getX() + 1], self.matrix[cell.getY() - 1][cell.getX() + 1],
                 self.matrix[cell.getY() - 1][cell.getX()]])
        elif cell.x == (self.size - 1) and cell.y == (self.size - 1):
            # Bottom Right corner
            cell.postNeighbors(
                [self.matrix[cell.getY()][cell.getX() - 1], self.matrix[cell.getY() - 1][cell.getX() - 1],
                 self.matrix[cell.getY() - 1][cell.getX()]])
        elif cell.y == 0:
            cell.postNeighbors(
                [self.matrix[cell.getY()][cell.getX() - 1], self.matrix[cell.getY()][cell.getX() + 1],
                 self.matrix[cell.getY() + 1][cell.getX() - 1], self.matrix[cell.getY() + 1][cell.getX()],
                 self.matrix[cell.getY() + 1][cell.getX() + 1]])
            # Top Edge
        elif cell.x == 0:
            # Left Edge
            cell.postNeighbors(
                [self.matrix[cell.getY() - 1][cell.getX()], self.matrix[cell.getY() + 1][cell.getX()],
                 self.matrix[cell.getY() - 1][cell.getX() + 1], self.matrix[cell.getY()][cell.getX() + 1],
                 self.matrix[cell.getY() + 1][cell.getX() + 1]])
        elif cell.x == (self.size - 1):
            # Right Edge
            cell.postNeighbors(
                [self.matrix[cell.getY() - 1][cell.getX()], self.matrix[cell.getY() + 1][cell.getX()],
                 self.matrix[cell.getY() + 1][cell.getX() - 1], self.matrix[cell.getY()][cell.getX() - 1],
                 self.matrix[cell.getY() - 1][cell.getX() - 1]])
        elif cell.y == (self.size - 1):
            # Bottom Edge
            cell.postNeighbors(
                [self.matrix[cell.getY()][cell.getX() - 1], self.matrix[cell.getY()][cell.getX() + 1],
                 self.matrix[cell.getY() - 1][cell.getX() - 1], self.matrix[cell.getY() - 1][cell.getX()],
                 self.matrix[cell.getY() - 1][cell.getX() + 1]])
        else:
            # All Surrounding Cells
            cell.postNeighbors(
                [self.matrix[cell.getY() - 1][cell.getX() - 1], self.matrix[cell.getY() - 1][cell.getX()],
                 self.matrix[cell.getY() - 1][cell.getX() + 1], self.matrix[cell.getY()][cell.getX() - 1],
                 self.matrix[cell.getY()][cell.getX() + 1], self.matrix[cell.getY() + 1][cell.getX() - 1],
                 self.matrix[cell.getY() + 1][cell.getX()], self.matrix[cell.getY() + 1][cell.getX() + 1]])

    def printFirstMatrix(self):
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                print(j, end=" ")
            print()

    def cycle(self):
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                j.prepUpdateCell()
        for i in range(len(self.matrix)):
            for j in self.matrix[i]:
                j.updateCell()
                print(j, end=" ")
            print()
