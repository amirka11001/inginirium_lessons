import pygame
pygame.init()
win=pygame.display.set_mode((600,400))
x=10
y=10
w=100
h=100
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    color=(255,255,255)
    win.fill(color)
    pygame.draw.rect(win,(255,0,0),(x,y,w,h))
    pygame.draw.line(win, (0, 255, 255), (0,0),(100,100),5)
    pygame.draw.circle(win, (255,0,0), (200, 200), 50)
    pygame.draw.lines(win, (0, 0, 0),True ,((200, 200),(300,150),(300,250)),10)
    pygame.draw.polygon(win, (0, 0, 0),[(0, 100), (100, 50), (100, 150)],False)
    pygame.display.update()