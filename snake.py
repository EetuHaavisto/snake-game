import pygame

SNAKE_RADIUS = 10 # 10 pixels wide

class Snake:

    def __init__(self, x, y):
        self.head = pygame.Rect(x,y,SNAKE_RADIUS,SNAKE_RADIUS)


    def move_snake(self, screen, delta_x, delta_y):
        # Get the coordinates for the old head
        old_ctr_x = self.head.centerx
        old_ctr_y = self.head.centery

        # Erase (fill with black) the old snake head
        pygame.draw.rect(surface=screen,color="black",rect=self.head)

        self.head.centerx = old_ctr_x + delta_x
        self.head.centery = old_ctr_y + delta_y
        pygame.draw.rect(surface=screen, color="green", rect=self.head)




