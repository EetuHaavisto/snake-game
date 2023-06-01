import pygame
from snake import Snake
from constants import *


class Snakebody(pygame.sprite.Sprite):

    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface((SNAKE_WIDTH, SNAKE_WIDTH))
        self.image.fill("green")
        self.rect = self.image.get_rect() # The end piece of tail

    def get_head_coordinates(self,snake):
        self.rect.x = snake.rect.x
        self.rect.y = snake.rect.y

    def new_end_piece(self, direction):

        # Parameters: dir: the direction in which user wants to move
        # snake_sprites: the spritegroup containing head + tail = full snake
        old_tail_x = self.rect.x
        old_tail_y = self.rect.y
        delta_x = 0
        delta_y = 0

        # Generate new tailpiece from the snake class:
        new_piece = Snake(is_head=False)
        # Check that the new tailpiece is build behind
        if direction == "UP":
            delta_x=0; delta_y = SNAKE_WIDTH
        elif direction == "DOWN":
            delta_x=0; delta_y = -SNAKE_WIDTH
        elif direction == "LEFT":
            delta_x = SNAKE_WIDTH; delta_y = 0
        elif direction == "RIGHT":
            delta_x = -SNAKE_WIDTH; delta_y = 0

        new_piece.rect.move_ip(old_tail_x+delta_x, old_tail_y + delta_y)
        # Set the new piece to be the next end piece of tail
        self.rect = new_piece.rect