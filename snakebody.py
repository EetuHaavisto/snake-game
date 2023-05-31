import pygame
import random
from constants import *


class Snakebody(pygame.sprite.Sprite):git gig

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_WIDTH, SNAKE_WIDTH))
        self.image.fill("green")
        self.rect = self.image.get_rect()