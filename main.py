import pygame
from constants import *
from snake import Snake
from food import Food
from snakebody import Snakebody


def main():
    pygame.init()

    # Game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
    pygame.display.set_caption("Snake")

    # Frame rate
    clock = pygame.time.Clock()

    # Help variables

    # Initialize game objects
    snake_head = Snake(SCREEN_WIDTH/2-SNAKE_WIDTH/2, SCREEN_HEIGTH/2-SNAKE_WIDTH/2, SNAKE_SPEED,"RIGHT", is_head=True)
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
                if event.key == pygame.K_LEFT and snake_head.dir != "RIGHT":
                    snake_head.dir = "LEFT"
                elif event.key == pygame.K_RIGHT and snake_head.dir != "LEFT":
                    snake_head.dir = "RIGHT"
                elif event.key == pygame.K_UP and snake_head.dir != "DOWN":
                    snake_head.dir = "UP"
                elif event.key == pygame.K_DOWN and snake_head.dir != "UP":
                    snake_head.dir = "DOWN"
        
        # Move snake head
        snake_head.update()

        # Move rest of the snake

        # If snake eats food
        if snake_head.rect.colliderect(food.rect):
            food.move_food()
            # When getting the first food and creating the first piece of tail:
            if len(snake_body_group.sprites()) == 1:
                new_piece = Snake(0,0,)

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