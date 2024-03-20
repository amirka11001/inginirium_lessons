import pygame
pygame.init()
win = pygame.display.set_mode((500, 450))
x = 100
y = 100
x1 = 250
y2 = 50
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    y2 = y2 + 1
    if y2 > 500:
     y2 = 0
    x = x + 1
    if x > 500:
        x = 1 - 1
    if y2 > 500:
        y2 = -1
    win.fill((255, 255, 255))
    pygame.draw.rect(win, (255, 255, 0), (x, y, 100, 150))
    pygame.draw.circle(win, (255, 0, 0), (x1, y2), 50)
    pygame.display.update()
    pygame.time.delay(10)
