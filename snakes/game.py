import pygame
from .constants import *
from .snake import Snake

class Game:

    def __init__(self, win):
        self.win = win
        self.snake = Snake()

    def _draw_window(self):
        # draw the background
        pygame.draw.rect(self.win, GREEN, (0, 0, WIDTH, HEIGHT))

        #draw the snake
        self.snake.update()
    
    def update(self):
        self._draw_window()
        pygame.display.update()