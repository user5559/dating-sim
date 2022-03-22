import pygame, os,ctypes
os.chdir('c://sidews')
from pygame.locals import(
    KEYDOWN,
    QUIT,
    RLEACCEL,
    K_ESCAPE

)
pygame.init()

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

screen = pygame.display.set_mode((screensize)) 

running = True



while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    screen.fill((255,182,193))
    pygame.display.update()
