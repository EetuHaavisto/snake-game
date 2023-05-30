import pygame, time
from snake import *
# game setup

pygame.init()
"""One surface is special -- the one you create with pygame.display.set_mode()
Initialize a window or screen for display. This 'display surface' represents the screen;
 whatever you do to it will appear on the user's screen."""
SPEED = 5
FPS = 60
TARGET_FPS = 60 # The original value in case we end up in a frame rate independent situation
SCREEN_DIMENSION = 800 # pixels

screen = pygame.display.set_mode((SCREEN_DIMENSION, SCREEN_DIMENSION))
running = True
clock = pygame.time.Clock()
snake = Snake(screen.get_width()/2-SNAKE_RADIUS, screen.get_height()/2+SNAKE_RADIUS)
# Default movement to the right:
#dir = "r" # up, down "d", left "l" or right "r"
delta_x = SPEED
delta_y = 0
screen.fill("black")
# Time settings
dt = 0
prev_time = time.time()

while running:
    now = time.time()
    dt = now-prev_time
    prev_time = now
    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != "d":
                delta_y = -SPEED; delta_x = 0;
                snake.direction = "u"

            if event.key == pygame.K_DOWN and snake.direction != "u":
                delta_y = SPEED; delta_x = 0;
                snake.direction = "d"

            if event.key == pygame.K_LEFT and snake.direction != "r":
                delta_y = 0; delta_x = -SPEED;
                snake.direction = "l"

            if event.key == pygame.K_RIGHT and snake.direction != "l":
                delta_y = 0; delta_x = SPEED;
                snake.direction = "r"

    snake.move_snake(screen, delta_x*dt*TARGET_FPS, delta_y*dt*TARGET_FPS)
    pygame.display.update() #pygame.display.flip() # Updates full screen, .update() updates part of the screen
    # Limit frame rate:
    clock.tick(FPS) # Tick = measure of time in PyGame.
    # clock.tick(40) means that for every second at most 40 frames should pass

pygame.quit()