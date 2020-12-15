import pygame
from .constants import *
from collections import deque

class Turn:

    def __init__(self, position, new_direction, bodies):
        self.position = position
        self.new_direction = new_direction
        self.body_id = deque(bodies)

    def __str__(self):
        return f'TURN: position = {self.position} | new direction = {self.new_direction}'

    def __repr__(self):
        return f'{__class__.__name__}({self.position}, {self.new_direction}, {list(self.body_id)})'

    def add_body_id(self, body_id):
        """Called when the snake eats a piece of fruit."""
        self.body_id.append(body_id)
    
    def remove(self, i):
        """Remove i from body_id, where i is the body segment that has just turned."""
        self.body_id.remove(i)