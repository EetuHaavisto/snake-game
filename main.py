import pygame

# game setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True

while running:

    # check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()