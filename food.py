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
        self.image = pygame.Surface((FOOD_WIDTH, FOOD_WIDTH))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.move_food()

    def move_food(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - FOOD_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGTH - FOOD_WIDTH)