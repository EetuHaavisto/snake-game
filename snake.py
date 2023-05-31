import pygame
from constants import SNAKE_WIDTH


class Snake(pygame.sprite.Sprite):
    """Part of a snake that will move
    Returns: SnakeBox object
    Methods: update, calcnewpos
    Attributes: area, vector"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_WIDTH, SNAKE_WIDTH))
        self.image.fill("green")
        self.rect = self.image.get_rect()

        # Movement variables
        self.speed = SNAKE_WIDTH / 2
        self.dir = "RIGHT"
        

    def update(self):
        if self.dir == "LEFT":
            self.rect.move_ip(-self.speed, 0)
        elif self.dir == "RIGHT":
            self.rect.move_ip(self.speed, 0)
        elif self.dir == "UP":
            self.rect.move_ip(0, -self.speed)
        else:
            self.rect.move_ip(0, self.speed)