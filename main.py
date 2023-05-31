import pygame
from constants import *
from snake import Snake
from food import Food

def main():
    pygame.init()

    # Game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("Snake")

    # Frame rate
    clock = pygame.time.Clock()

    # Help variables

    # Initialize game objects
    snake_head = Snake()
    food = Food()

    # sprite.Group for snake body
    snake_body_group = pygame.sprite.Group()
    snake_body_group.add(snake_head)

    #sprite.Group for food
    food_group = pygame.sprite.Group()
    food_group.add(food)
    
    # Game loop
    running = True
    while running:
        
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # User presses LEFT/RIGHT/UP/DOWN
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_head.dir = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    snake_head.dir = "RIGHT"
                elif event.key == pygame.K_UP:
                    snake_head.dir = "UP"
                elif event.key == pygame.K_DOWN:
                    snake_head.dir = "DOWN"
        
        # Move snake head
        snake_head.update()

        # If snake eats food
        if snake_head.rect.colliderect(food.rect):
            food.move_food()

        # Backgroud / Erase previous frame
        screen.fill("grey")

        # Draw sprites
        snake_body_group.draw(screen)
        food_group.draw(screen)

        # Update display
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()