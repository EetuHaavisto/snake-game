import pygame
from constants import *


class Snake(pygame.sprite.Sprite):
    """Part of a snake that will move
    Returns: SnakeBox object
    Methods: update, calcnewpos
    Attributes: area, vector"""
    def __init__(self, x, y, speed, direction, is_head = True):
         # Call the parent class (Sprite) constructor
        super().__init__()
        #pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_WIDTH, SNAKE_WIDTH))
        self.image.fill("green")
        self.rect = self.image.get_rect()

        #self.rect.x = SCREEN_WIDTH/2-SNAKE_WIDTH/2
        #self.rect.y = SCREEN_HEIGTH/2-SNAKE_WIDTH/2
        self.rect.x = x
        self.rect.y = y

        # Check if the created snake piece is head or tail
        self.is_head = is_head
        # Movement variables
        self.speed = speed
        self.dir = direction


    def update(self):

        if self.dir == "LEFT":
            self.rect.move_ip(-self.speed, 0)
        elif self.dir == "RIGHT":
            self.rect.move_ip(self.speed, 0)
        elif self.dir == "UP":
            self.rect.move_ip(0, -self.speed)
        else:
            self.rect.move_ip(0, self.speed)

    def get_head_coordinates(self, snake):
        # Get the coordinates from the previous snake piece to build the new one correctly
        self.rect.x = snake.rect.x
        self.rect.y = snake.rect.y