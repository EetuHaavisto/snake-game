import pygame

SNAKE_RADIUS = 10 # 2*10 pixels wide
SNAKE_DIRECTION = "r"
class Snake:

    def __init__(self, x, y):
        self.head = pygame.Rect(x,y,SNAKE_RADIUS,SNAKE_RADIUS)
        self.direction = SNAKE_DIRECTION

    def move_snake(self, screen, delta_x, delta_y):
        # Get the coordinates for the old head
        old_ctr_x = self.head.centerx
        old_ctr_y = self.head.centery

        # Erase (fill with black) the old snake head
        pygame.draw.rect(surface=screen,color="black",rect=self.head)

        self.head.centerx = old_ctr_x + delta_x
        self.head.centery = old_ctr_y + delta_y
        # Add (fill with green) the new snake head
        pygame.draw.rect(surface=screen, color="green", rect=self.head)

    def get_head_center_coord(self):
        x = self.head.centerx
        y = self.head.centery
        return (x,y)


