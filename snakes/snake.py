import pygame
from .constants import *
from collections import deque, namedtuple

class Snake:

    def __init__(self, win):
        self.win = win

        self.speed = START_SPEED
        self.direction = RIGHT
        self.alive = True

        self.start_pos = (WIDTH//2, HEIGHT//2)
        self.snake = deque([self.start_pos])
        self.turns = deque()
        self.path = deque()
    
    def __str__(self):
        return f'SNAKE: length = {len(self.snake)} | speed = {self.speed} | direction = {self.direction}'
    
    def __repr__(self):
        return f'{__class__.__name__}({repr(self.win)})'
    
    def _draw_snake(self):
        for seg in self.snake:
            x, y = seg
            pygame.draw.rect(self.win, BROWN, (x, y, BODY_WIDTH, BODY_HEIGHT))
    
    def _update_path(self):
        self.path.appendleft(self.body[0])
        while len(self.path) > len(self.body) - 1:
            self.path.pop()
    
    def get_head(self):
        return self.snake[0]
    
    def grow(self):
        """When the snake eats fruit this method is called to increase the length of the snake."""
        x_last, y_last = self.snake[-1]

        if self.direction == RIGHT or self.direction == LEFT:
            pos = (x_last - (self.direction[0] * len(self.snake) * BODY_WIDTH), y_last)
        else:
            pos = (x_last, y_last - (self.direction[1] * len(self.snake) * BODY_HEIGHT))
        
        self.snake.append(pos)

    def move(self):
        """Increase the position of each body segment with respect to the direction."""
        self._update_path()

        x_vel, y_vel = tuple(map(lambda d: d * self.speed, self.direction))
        x_head, y_head = self.snake[0]
        self.body[0] = (x_vel + x_head, y_vel + y_head)

        for i in range(1, len(self.snake)):
            path_index = i - 1

            x_path, y_path = self.path[path_index]
            if self.direction == RIGHT or self.direction == LEFT:
                self.body[i] = (x_path - (self.direction[0] * i * BODY_WIDTH), y_path)
            else:
                self.body[i] = (x_path, y_path - (self.direction[1] * i * BODY_HEIGHT))

            path_index += 1

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
        x_pos, y_pos = self.snake[0]  # snake head always at index 0

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
