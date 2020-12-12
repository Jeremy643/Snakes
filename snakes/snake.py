import pygame
from .constants import *
from collections import deque

class Snake:

    def __init__(self, win):
        self.win = win
        self.start_pos = (WIDTH//2, HEIGHT//2)
        self.body = deque([self.start_pos])

        self.speed = START_SPEED
        self.direction = RIGHT
    
    def __str__(self):
        return f'SNAKE: length = {len(self.body)} | speed = {self.speed} | direction = {self.direction}'
    
    def __repr__(self):
        return f'{__class__.__name__}({repr(self.win)})'
    
    def _draw_snake(self):
        for seg in self.body:
            x, y = seg
            pygame.draw.rect(self.win, BROWN, (x, y, BODY_WIDTH, BODY_HEIGHT))
    
    def move(self):
        """Increase the position of each body segment with respect to the direction."""
        pass

    def change_direction(self, snake_dir):
        """Change the direction of the snake based on the user's input."""
        self.direction = snake_dir

    def update(self):
        self._draw_snake()
