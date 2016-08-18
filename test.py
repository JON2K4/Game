import pygame
import pygame.gfxdraw
from pygame.locals import *
from OpenGL import *

pygame.init()
screen = pygame.display.set_mode((400, 400))

bg = pygame.Surface(screen.get_size()).convert()
p = pygame.Surface((20, 20), SRCALPHA)
pygame.gfxdraw.line(p, 10, 10, 20, 20, (255, 255, 255))

i = 0

clk = pygame.time.Clock()
run = True
dir = True
while run:
    bg.fill((0, 0, 0))
    clk.tick(10)
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            run = False

    pygame.gfxdraw.vline(bg, i, 0, 400, (255, 255, 255))
    pygame.gfxdraw.hline(bg, 0, 400, i, (255, 255, 255))

    x = pygame.math.Vector2((200, 50))

    bg.blit(p, (100, 100))
    screen.blit(bg, (0, 0))
    pygame.display.update()

    if dir:
        i += 5
    else:
        i -= 5

    if i >= 400:
        dir = False
    elif i <= 0:
        dir = True