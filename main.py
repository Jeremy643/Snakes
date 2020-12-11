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

    # TODO: Figure out pygame.set_allowed()

    # limit the pygame events allowed in the queue
    # pygame.event.set_allowed(pygame.KEYDOWN)
    # print(pygame.event.get_blocked(pygame.MOUSEBUTTONDOWN))

    clock_tick = clock.tick
    while run:
        clock_tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.user_input(UP)
                elif event.key == pygame.K_RIGHT:
                    game.user_input(RIGHT)
                elif event.key == pygame.K_DOWN:
                    game.user_input(DOWN)
                elif event.key == pygame.K_LEFT:
                    game.user_input(LEFT)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     print('wrong')
        
        game.update()
    
    pygame.quit()


if __name__ == '__main__':
    main()