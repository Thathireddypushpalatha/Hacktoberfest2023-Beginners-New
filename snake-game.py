import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
SNAKE_SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake initial position
x, y = WIDTH // 2, HEIGHT // 2
x_change, y_change = 0, 0
snake_body = [(x, y)]

# Food initial position
food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)

score = 0

font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -SNAKE_SIZE
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = SNAKE_SIZE
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -SNAKE_SIZE
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = SNAKE_SIZE

    # Move the snake
    x += x_change
    y += y_change
    snake_body.append((x, y))

    # Check for collisions
    if len(snake_body) > 1 and (x, y) in snake_body[:-1]:
        running = False

    # Check for collision with food
    if x == food_x and y == food_y:
        score += 1
        food_x = random.randrange(0, WIDTH - SNAKE_SIZE, SNAKE_SIZE)
        food_y = random.randrange(0, HEIGHT - SNAKE_SIZE, SNAKE_SIZE)
    else:
        snake_body.pop(0)

    # Draw the screen
    screen.fill(BLACK)
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    
    pygame.draw.rect(screen, RED, (food_x, food_y, SNAKE_SIZE, SNAKE_SIZE))

    # Display score
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.update()

    # Control game speed
    pygame.time.delay(100)

# Game over screen
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render("Game Over", True, WHITE)
screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 36))
pygame.display.update()
pygame.time.delay(2000)  # Wait for 2 seconds before quitting

# Quit Pygame
pygame.quit()
