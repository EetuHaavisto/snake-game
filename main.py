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
    snake_head = Snake()
    food = Food()

    # sprite.Groups for snake
    snake_head_group = pygame.sprite.Group()
    snake_head_group.add(snake_head)
    snake_tail_group = pygame.sprite.Group()

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
                elif event.key == pygame.K_DOWN and snake_head.dir != "UPgit sta":
                    snake_head.dir = "DOWN"
        
        # Move snake head
        snake_head_group.update()

        # If snake eats food
        if snake_head.rect.colliderect(food.rect):
            food.move_food()
            # Add new snake body part to group
            snake_tail_group.add(Snakebody(snake_head.get_num_of_bodies()))
            snake_head.add_num_of_bodies()

        # Move snake tail parts
        snake_tail_group.update(snake_head.previous_locations)

        # DRAW NEW FRAME
        screen.fill(GREY)

        # Draw snake and food
        snake_head_group.draw(screen)
        snake_tail_group.draw(screen)
        food_group.draw(screen)

        # Update display
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()