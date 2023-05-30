import pygame


class Snake:

    def __init__(self, x_coord, y_coord, color):

        self.x = x_coord
        self.y = y_coord
        self.color = color


    def move_snake(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def draw_snake(self, screen):

        pos = pygame.Vector2(self.x, self.y)
        rad = 5 # 5 pixels as radius
        pygame.draw.circle(screen,self.color,pos,rad)