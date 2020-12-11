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
        x = randint(0, WIDTH)
        y = randint(0, HEIGHT)
        return (x, y)
    
    def _draw_fruit(self):
        # TODO: Replace rectange with sprite. 
        pygame.draw.rect(self.win, YELLOW, (*self.position, 15, 15))
    
    def update(self):
        self._draw_fruit()