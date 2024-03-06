import pygame
import random

# Initialize pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Set up display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
FONT_SIZE = 30
FPS = 10

# Define directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

# Define game variables
score = 0
snake = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
food = (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)
direction = RIGHT
clock = pygame.time.Clock()

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont(None, FONT_SIZE)


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))


def draw_food(food):
    pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))


def move_snake(snake, direction):
    head = list(snake[0])
    if direction == UP:
        head[1] -= BLOCK_SIZE
    elif direction == DOWN:
        head[1] += BLOCK_SIZE
    elif direction == LEFT:
        head[0] -= BLOCK_SIZE
    elif direction == RIGHT:
        head[0] += BLOCK_SIZE
    snake.insert(0, tuple(head))


def generate_food():
    return (random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE)


def check_collision(snake):
    head = snake[0]
    if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
        return True
    if head in snake[1:]:
        return True
    return False


def main():
    global direction, score, food

    running = True
    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    if direction != DOWN:
                        direction = UP
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if direction != UP:
                        direction = DOWN
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if direction != RIGHT:
                        direction = LEFT
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if direction != LEFT:
                        direction = RIGHT

        move_snake(snake, direction)

        if snake[0] == food:
            score += 1
            food = generate_food()
        else:
            snake.pop()

        if check_collision(snake):
            running = False

        draw_snake(snake)
        draw_food(food)

        score_text = font.render("Score: " + str(score), True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
