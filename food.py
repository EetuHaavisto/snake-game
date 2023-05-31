import pygame
import random
from constants import *

class Food(pygame.sprite.Sprite):
    """Food that the snake eats
    Returns: Food object
    Methods:
    Attributes:
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_WIDTH/2, SNAKE_WIDTH/2))
        self.image.fill("red")
        self.rect = self.image.get_rect()
        self.move_food()

    def move_food(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - 5)
        self.rect.y = random.randint(0, SCREEN_HEIGTH - 5)