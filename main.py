from matrix import matrix
import time

size = int(input("What is the size? "))

life = matrix(size)
life.printFirstMatrix()
while True:
    time.sleep(.1)
    life.cycle()
