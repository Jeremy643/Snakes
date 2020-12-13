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
    
    def _fruit_eaten(self):
        x_head, y_head = self.snake.get_head()
        x_fruit, y_fruit = self.fruit.position

        x_snake_cov = set(range(x_head, x_head + BODY_WIDTH + 1))
        y_snake_cov = set(range(y_head, y_head + BODY_HEIGHT + 1))

        x_fruit_cov = set(range(x_fruit, x_fruit + FRUIT_WIDTH + 1))
        y_fruit_cov = set(range(y_fruit, y_fruit + FRUIT_HEIGHT + 1))

        if (x_snake_cov & x_fruit_cov) and (y_snake_cov & y_fruit_cov):
            self.snake.grow()
            self.fruit.eat()
            return True
        
        return False
            
    def user_input(self, snake_dir):
        """Handles the user's input."""
        self.snake.change_direction(snake_dir)
    
    def update(self):
        """Draw background, snake and fruit then update pygame window."""
        self._draw_window()

        # check if snake eats fruit
        self._fruit_eaten()

        pygame.display.update()
