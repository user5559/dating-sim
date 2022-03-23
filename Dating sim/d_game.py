import pygame, os,ctypes
os.chdir('c://Dating sim')
from pygame.locals import(
    KEYDOWN,
    QUIT,
    RLEACCEL,
    K_ESCAPE

)
pygame.init()

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
screensize = list(screensize)
SCREEN_WIDTH = screensize[0]
SCREEN_HEIGHT = screensize[1]

screen = pygame.display.set_mode((screensize)) 

running = True

background_color = 255,182,193
#255,182,193
Rickimage = pygame.image.load('gorrillaz.png')
text_box = pygame.image.load('dating sim textbox.png')

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
    
    screen.fill((background_color))

    screen.blit(Rickimage, (SCREEN_WIDTH/2.5, SCREEN_HEIGHT/4))
    screen.blit(text_box, (SCREEN_WIDTH, SCREEN_HEIGHT))



    pygame.display.update()
