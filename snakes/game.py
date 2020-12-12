import pygame
from .constants import *
from .snake import Snake
from .fruit import Fruit

class Game:

    def __init__(self, win):
        self.win = win
        self.snake = Snake(win)
        self.fruit = Fruit(win)
    
    def __str__(self):
        return f'{str(self.snake)}\n{str(self.fruit)}'

    def __repr__(self):
        return f'{__class__.__name__}({repr(self.win)})'

    def _draw_window(self):
        # draw the background
        pygame.draw.rect(self.win, GREEN, (0, 0, WIDTH, HEIGHT))

        # draw the snake and fruit
        self.snake.update()
        self.fruit.update()
    
    def user_input(self, snake_dir):
        """Handles the user's input."""
        self.snake.change_direction(snake_dir)
    
    def update(self):
        """Draw background, snake and fruit then update pygame window."""
        self._draw_window()
        pygame.display.update()
