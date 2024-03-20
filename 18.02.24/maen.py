import random

import pygame
pygame.init()
width = 500
height = 500

win = pygame.display.set_mode((width, height))


class Circle():
    def __init__(self, color, x, y, rad, dir):
        self.color = color
        self.x = x
        self.y = y
        self.rad = rad
        self.dir = 'right'

    def draw(self):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def horisontal_movements(self):
        if self.dir

krug = Circle((255, 0, 0), width / 2, height / 2, 30)

FPS = 60
clock = pygame.time.Clock()



krugi = []
for i in range(100):
    krugi.append(Circle(random.choices(range(256), k=3), i * 10, i * 5, 30))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    win.fill((255, 255, 255))

    for i in range(len(krugi)):
        krugi[i].draw()
        krugi[i].horisontal_movements()
    pygame.display.update()
    clock.tick(FPS)
