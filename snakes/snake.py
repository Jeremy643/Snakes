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
        self.alive = True
    
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
        x_vel, y_vel = tuple(map(lambda d: d * self.speed, self.direction))
        for i in range(len(self.body)):
            x_body, y_body = self.body[i]
            self.body[i] = (x_vel + x_body, y_vel + y_body)

    def change_direction(self, snake_dir):
        """Change the direction of the snake based on the user's input."""
        if self.direction == RIGHT and snake_dir == LEFT or self.direction == LEFT and snake_dir == RIGHT:
            return False
        if self.direction == UP and snake_dir == DOWN or self.direction == DOWN and snake_dir == UP:
            return False

        self.direction = snake_dir
        return True
    
    def touching_boundary(self):
        """Check if the snake is touching any of the boundaries."""
        x_pos, y_pos = self.body[0]  # snake head always at index 0

        if y_pos == 0 or x_pos == (WIDTH - BODY_WIDTH) or y_pos == (HEIGHT - BODY_HEIGHT) or x_pos == 0:
            return True
        
        return False

    def check_alive(self):
        """If snake touches boundary it dies and stops moving."""
        if self.touching_boundary():
            self.alive = False
            self.speed = 0

    def update(self):
        self.check_alive()
        self.move()
        self._draw_snake()
