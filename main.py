import pygame
from snake import *
# game setup

pygame.init()
"""One surface is special -- the one you create with pygame.display.set_mode()
Initialize a window or screen for display. This 'display surface' represents the screen;
 whatever you do to it will appear on the user's screen."""
screen = pygame.display.set_mode((800, 800))
running = True


MOVE = pygame.USEREVENT+0
clock = pygame.time.Clock()
pygame.time.set_timer(MOVE,500)
snake = Snake(screen.get_width()/2-SNAKE_RADIUS, screen.get_height()/2+SNAKE_RADIUS)

screen.fill("black")

while running:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOVE:
            snake.move_snake(screen,2*SNAKE_RADIUS,0)



    pygame.display.update()
    #pygame.display.flip() # Updates full screen, .update() updates part of the screen
    clock.tick(60)
pygame.quit()