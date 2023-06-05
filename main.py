from matrix import matrix
import time

size = int(input("What is the size? "))

life = matrix(size)
life.printFirstMatrix()
print()
life.updateMatrix()
'''
while True:
    time.sleep(2)
    life.updateMatrix()
'''