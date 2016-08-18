'''

'''

import sys
import pygame
from pygame import time, PixelArray
from pygame.locals import *

from world import World
from character import *

def start_screen(screen_size, clk_rate):
    pygame.init()
    clk = pygame.time.Clock()

    window = pygame.display
    window.set_mode(screen_size)

    bg = Stage(window, (0, 0), window.get_surface().get_size(), (15, 15, 15, 255))

    title = Text_Img(bg, (55, 55, 55, 255), (250, 250), "TEST", 24)

    run = True
    while run:
        clk.tick(clk_rate)

        title.set_size(24)
        title.draw()

        bg.update()
        pygame.display.update()
        pygame.time.delay(200)
        bg.clear()

        title.set_size(72)
        title.draw()

        bg.update()
        pygame.display.update()
        pygame.time.delay(200)
        bg.clear()

        for event in pygame.event.get():
            if event.type is QUIT:
                sys.exit()

            if event.type is KEYDOWN:
                if event.key == K_SPACE:
                    run = False


def main(screen_size, clk_rate):
    pygame.init()
    clk = pygame.time.Clock()
    window = pygame.display
    window.set_mode(screen_size)
    pygame.key.set_repeat(15, 0)

    world = World(window, clk)

    plr = Player(world, (20, 250))

    frame = 0
    run = True
    while run:
        clk.tick(clk_rate)
        frame += 1

        for event in pygame.event.get():
            if event.type is QUIT:
                run = False

            if event.type is KEYDOWN:
                if event.key == K_RIGHT:
                    plr.move(1)

                if event.key == K_LEFT:
                    plr.move(-1)

        plr.draw()

        world.update_world()

if __name__ == "__main__":
    start_screen([500, 500], 60)
    main([500, 500], 60)
