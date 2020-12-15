import pygame
from .constants import *
from .turn import Turn
from collections import deque, namedtuple

class Snake:

    def __init__(self, win):
        self.win = win

        self.speed = START_SPEED
        self.direction = RIGHT
        self.alive = True

        self.start_pos = (WIDTH//2, HEIGHT//2)
        self.body = namedtuple('body', ['position', 'direction'])
        self.snake = deque([self.body(self.start_pos, self.direction)])
        self.turns = deque()
    
    def __str__(self):
        return f'SNAKE: length = {len(self.snake)} | speed = {self.speed} | direction = {self.direction}'
    
    def __repr__(self):
        return f'{__class__.__name__}({repr(self.win)})'
    
    def _draw_snake(self):
        for seg in self.snake:
            x, y = seg.position
            pygame.draw.rect(self.win, BROWN, (x, y, BODY_WIDTH, BODY_HEIGHT))
    
    def _get_next_turn(self, body_id):
        for turn in self.turns:
            if body_id in turn.body_id:
                return turn
        return None
    
    def _remove_turns(self):
        """Remove the turns that all parts of the snake have been through."""
        try:
            if not self.turns[0].body_id:
                return self.turns.popleft()
        except IndexError:
            return None
        
    def _new_body_turns(self):
        for turn in self.turns:
            turn.add_body_id(len(self.snake)-1)
    
    def _make_turn(self, turn, i):
        new_pos = turn.position
        direction = turn.new_direction
        turn.remove(i)
        return new_pos, direction
    
    def get_head(self):
        return self.snake[0].position
    
    def grow(self):
        """When the snake eats fruit this method is called to increase the length of the snake."""
        x_last, y_last = self.snake[-1].position

        if self.snake[-1].direction == RIGHT or self.snake[-1].direction == LEFT:
            pos = (x_last - (self.snake[-1].direction[0] * BODY_WIDTH), y_last)
        else:
            pos = (x_last, y_last - (self.snake[-1].direction[1] * BODY_HEIGHT))
        
        new_body = self.body(pos, self.snake[-1].direction)
        self.snake.append(new_body)
        self._new_body_turns()

    def move(self):
        """Increase the position of each body segment with respect to the direction."""
        for i in range(len(self.snake)):
            x_vel, y_vel = tuple(map(lambda d: d * self.speed, self.snake[i].direction))
            x_body, y_body = self.snake[i].position
            new_pos = (x_vel + x_body, y_vel + y_body)
            direction = self.snake[i].direction

            if i > 0:
                next_turn = self._get_next_turn(i)
                x_min, x_max = min(x_body, new_pos[0]), max(x_body, new_pos[0])
                y_min, y_max = min(y_body, new_pos[1]), max(y_body, new_pos[1])
                if next_turn and (next_turn.position[0] in range(x_min, x_max + 1) and next_turn.position[1] in range(y_min, y_max + 1)):
                    new_pos, direction = self._make_turn(next_turn, i)

            self.snake[i] = self.body(new_pos, direction)

    def change_direction(self, snake_dir):
        """Change the direction of the snake based on the user's input."""
        if self.direction == RIGHT and snake_dir == LEFT or self.direction == LEFT and snake_dir == RIGHT:
            return False
        if self.direction == UP and snake_dir == DOWN or self.direction == DOWN and snake_dir == UP:
            return False

        # add new turn
        new_turn = Turn(self.snake[0].position, snake_dir, list(range(1, len(self.snake))))
        self.turns.append(new_turn)
        
        self.direction = snake_dir
        self.snake[0] = self.body(self.snake[0].position, snake_dir)
        return True
    
    def touching_boundary(self):
        """Check if the snake is touching any of the boundaries."""
        x_pos, y_pos = self.snake[0].position  # snake head always at index 0

        if y_pos == 0 or x_pos >= (WIDTH - BODY_WIDTH) or y_pos >= (HEIGHT - BODY_HEIGHT) or x_pos == 0:
            return True
        
        return False
    
    def eaten_itself(self):
        """Determines if the snake bites its tail."""
        try:
            x_head, y_head = self.snake[0].position
            x_second, y_second = self.snake[1].position
            x_last, y_last = self.snake[-1].position

            x_min, x_max = min(x_second, x_last), max(x_second, x_last)
            y_min, y_max = min(y_second, y_last), max(y_second, y_last)
            if x_head in range(x_min, x_max) and y_head in range(y_min, y_max):
                return True
            
            return False
        except IndexError:
            return False

    def check_alive(self):
        """If snake touches boundary it dies and stops moving."""
        if self.touching_boundary() or self.eaten_itself():
            self.alive = False
            self.speed = 0

    def update(self):
        self.check_alive()
        self.move()
        self._remove_turns()
        self._draw_snake()
