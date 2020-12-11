import pygame
from .constants import *
from collections import deque

class Snake:

    def __init__(self, win):
        self.win = win
        self.start_pos = (WIDTH//2, HEIGHT//2)
        self.body = deque([self.start_pos])
    
    def _draw_snake(self):
        for seg in self.body:
            x, y = seg
            pygame.draw.rect(self.win, BROWN, (x, y, BODY_WIDTH, BODY_HEIGHT))

    def update(self):
        self._draw_snake()