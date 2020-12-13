import pygame
from random import randint
from .constants import *

class Fruit:

    def __init__(self, win):
        self.win = win
        self.position = self._pick_position()
    
    def __str__(self):
        return f'FRUIT: position = {self.position}'
    
    def __repr__(self):
        return f'{__class__.__name__}({repr(self.win)})'
    
    def _pick_position(self):
        """Pick a random location for the fruit."""
        x = randint(0, WIDTH - FRUIT_WIDTH)
        y = randint(0, HEIGHT - FRUIT_HEIGHT)
        return (x, y)
    
    def _draw_fruit(self):
        # TODO: Replace rectange with sprite. 
        pygame.draw.rect(self.win, YELLOW, (*self.position, FRUIT_WIDTH, FRUIT_HEIGHT))
    
    def eat(self):
        # change the position of the fruit
        self.position = self._pick_position()
    
    def update(self):
        self._draw_fruit()
