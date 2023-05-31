import pygame
from constants import *
from collections import deque


class Snake(pygame.sprite.Sprite):
    """Part of a snake that will move
    Returns: SnakeBox object
    Methods: update, calcnewpos
    Attributes: area, vector"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_WIDTH, SNAKE_WIDTH))
        self.image.fill(GREEN_HEAD)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH/2
        self.rect.y = SCREEN_HEIGTH/2

        # Attributes for controlling the body of the snake
        self.number_of_bodies = 0
        self.previous_locations = deque([], maxlen=SCREEN_WIDTH*SCREEN_HEIGTH)

        # Movement attributes
        self.speed = SNAKE_SPEED
        self.dir = "RIGHT"
    
    def get_location(self):
        location = (self.rect.x, self.rect.y)
        return location
    
    def get_num_of_bodies(self):
        return self.number_of_bodies
    
    def add_num_of_bodies(self):
        self.number_of_bodies += 1

    def update_previous_locations(self):
        self.previous_locations.appendleft(self.get_location())
        # We only need to keep track of number_of_bodies+1 previous head positions
        if len(self.previous_locations) > self.number_of_bodies + 1:
            self.previous_locations.pop()

    def update(self):
        # Add position to previous positions
        self.update_previous_locations()

        if self.dir == "LEFT":
            self.rect.move_ip(-self.speed, 0)
        elif self.dir == "RIGHT":
            self.rect.move_ip(self.speed, 0)
        elif self.dir == "UP":
            self.rect.move_ip(0, -self.speed)
        elif self.dir == "DOWN":
            self.rect.move_ip(0, self.speed)