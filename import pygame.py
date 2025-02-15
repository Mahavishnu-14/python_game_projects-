import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Snake settings
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = "RIGHT"
change_to = direction
speed = 15

# Food settings
food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
food_spawn = True

def game_over():
    pygame.quit()
    quit()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            elif event.key == pygame.K_DOWN:
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT:
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    elif change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    if direction == "UP":
        snake_pos[1] -= 10
    elif direction == "DOWN":
        snake_pos[1] += 10
    elif direction == "LEFT":
        snake_pos[0] -= 10
    elif direction == "RIGHT":
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))
    if snake_pos == food_pos:
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (WIDTH // 10)) * 10, random.randrange(1, (HEIGHT // 10)) * 10]
    food_spawn = True

    screen.fill(WHITE)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    if snake_pos[0] < 0 or snake_pos[0] > WIDTH-10 or snake_pos[1] < 0 or snake_pos[1] > HEIGHT-10:
        game_over()

    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    pygame.display.update()
    clock.tick(speed)
