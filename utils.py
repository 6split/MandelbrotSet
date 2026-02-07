import pygame

def arrayToScreen(array, screen):
    xcount = 0
    for x in array:
        xcount+=1
        ycount = 0
        for y in x:
            if y == 0:
                pygame.draw.line(screen, pygame.color.Color(255,255,255), (xcount, ycount), (xcount, ycount))
            else:
                pygame.draw.line(screen, pygame.color.Color(0,0,0), (xcount, ycount), (xcount, ycount))
            ycount += 1

def z(n, c):
    if n == 0:
        return 0
    else:
        return z(n - 1, c) ** 2 + c\

def znonrecursive(n, c):
    z = 0
    for i in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return z
    return z

def mandelbrot(depth ,candidate, start):
    return znonrecursive(depth, c=candidate)

#need a function to generate an array with x -2 to .5 and y from -1.5 to 1.5
def generation(min, max, divisions):
    jumpvalue = float((max - min)/divisions)
    value = []
    tempvalue = min
    while tempvalue <= max:
        value.append(tempvalue)
        tempvalue += jumpvalue
    return value
