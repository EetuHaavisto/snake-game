import pygame
from snake import *
# game setup

pygame.init()
"""One surface is special -- the one you create with pygame.display.set_mode()
Initialize a window or screen for display. This 'display surface' represents the screen;
 whatever you do to it will appear on the user's screen."""
screen = pygame.display.set_mode((800, 800))
running = True

SPEED = 2*SNAKE_RADIUS
MOVE = pygame.USEREVENT+0
clock = pygame.time.Clock()
pygame.time.set_timer(MOVE,500)
snake = Snake(screen.get_width()/2-SNAKE_RADIUS, screen.get_height()/2+SNAKE_RADIUS)
# Default movement to the right:
dir = "r" # up, down "d", left "l" or right "r"
delta_x = SPEED
delta_y = 0
screen.fill("black")

while running:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == MOVE:
            snake.move_snake(screen, delta_x, delta_y)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != "d":
                delta_y = -SPEED; delta_x = 0;
                dir = "u"

            if event.key == pygame.K_DOWN and dir != "u":
                delta_y = SPEED; delta_x = 0;
                dir = "d"

            if event.key == pygame.K_LEFT and dir != "r":
                delta_y = 0; delta_x = -SPEED;
                dir = "l"

            if event.key == pygame.K_RIGHT and dir != "l":
                delta_y = 0; delta_x = SPEED;
                dir = "r"
    pygame.display.update()
    #pygame.display.flip() # Updates full screen, .update() updates part of the screen
    clock.tick(60)
pygame.quit()