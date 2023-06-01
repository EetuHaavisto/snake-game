import pygame
from constants import SNAKE_WIDTH, GREEN_BODY


class Snakebody(pygame.sprite.Sprite):

    def __init__(self, distance_from_head):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((SNAKE_WIDTH, SNAKE_WIDTH))
        self.image.fill(GREEN_BODY)
        self.rect = self.image.get_rect()

        # Attribute which tells the "distance" from head. 
        # First tailblock from head = 0, second = 1, ...
        self.distace_from_head = distance_from_head

    def update(self, head_positions):
        self.rect.x = head_positions[self.distace_from_head][0]
        self.rect.y = head_positions[self.distace_from_head][1]