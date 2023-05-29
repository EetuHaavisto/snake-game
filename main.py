import pygame
from snake import *
# game setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

snake = Snake(screen.get_width()/2, screen.get_height()/2,"white")

while running:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    snake.draw_snake(screen)


    pygame.display.flip() # Updates full screen, .update() updates part of the screen
pygame.quit()