import pygame
import os
from snakes.constants import *
from snakes.game import Game


pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (100, 100)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snakes')

FPS = 60

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        game.update()
    
    pygame.quit()


if __name__ == '__main__':
    main()