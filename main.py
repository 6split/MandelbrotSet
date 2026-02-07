import pygame
from utils import *
import time

iterations = 15
rows, cols = (700,700)
pygame.init()
screen = pygame.display.set_mode((rows, cols))
clock = pygame.time.Clock()
running = True
array = [[0 for i in range(cols)] for j in range(rows)]
theactualnumberarray = [[0 for i in range(cols)] for j in range(rows)]
realnumbers = generation(-2, 0.5, rows)
print(len(realnumbers))
imaginary = generation(-1.5, 1.5, cols)
for x in range(len(realnumbers) - 1):
    for y in range(len(imaginary) - 1):
        theactualnumberarray[x][y] = realnumbers[x] + imaginary[y] * 1j
for x in range(len(array)):
    for y in range(len(array[0])):
        if abs(mandelbrot(iterations, theactualnumberarray[x][y], start=0)) < 2:
            array[x][y] = 1
        else:
            array[x][y] = 0
arrayToScreen(array, screen)
pygame.display.flip()

while running:
    time.sleep(10)

