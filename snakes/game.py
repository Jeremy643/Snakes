import pygame
from snake import Snake

class Game:

    def __init__(self, win):
        self.win = win
        self.snake = Snake()