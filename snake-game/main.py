import pygame
import random

# Initialize Pygame
pygame.init()

# Define constants for screen dimensions and game parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20
INITIAL_SNAKE_SIZE = 3
SNAKE_SPEED = 200  # Milliseconds per frame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define directions for the snake
class Direction:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

# Function to create the game window
def create_window():
    return pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Function to initialize game variables
def initialize_game():
    snake = [(4, 4)] * INITIAL_SNAKE_SIZE  # Initialize the snake with a few segments
    direction = Direction.RIGHT
    food = generate_food_position(snake)
    score = 0
    return snake, direction, food, score

# Function to generate a random position for the food
def generate_food_position(snake):
    while True:
        food = (random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE)
        if food not in snake:
            return food

# Function to handle user input
def handle_input(direction):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != Direction.DOWN:
                return Direction.UP
            elif event.key == pygame.K_DOWN and direction != Direction.UP:
                return Direction.DOWN
            elif event.key == pygame.K_LEFT and direction != Direction.RIGHT:
                return Direction.LEFT
            elif event.key == pygame.K_RIGHT and direction != Direction.LEFT:
                return Direction.RIGHT
    return direction

# Function to move the snake
def move_snake(snake, direction):
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)
    snake.insert(0, new_head)

# Function to check if the snake has collided with the wall or itself
def check_collision(snake):
    head = snake[0]
    if (head[0] < 0 or head[0] >= SCREEN_WIDTH or
            head[1] < 0 or head[1] >= SCREEN_HEIGHT or
            head in snake[1:]):
        return True
    return False

# Function to draw the snake and food on the screen
def draw_game(screen, snake, food):
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))
    pygame.display.update()

def main():
    screen = create_window()
    clock = pygame.time.Clock()
    snake, direction, food, score = initialize_game()

    running = True
    last_update_time = 0

    while running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_update_time

        if elapsed_time >= SNAKE_SPEED:
            direction = handle_input(direction)
            move_snake(snake, direction)
            if check_collision(snake):
                running = False

            # Check if the snake ate the food
            if snake[0] == food:
                score += 1
                food = generate_food_position(snake)
            else:
                snake.pop()

            draw_game(screen, snake, food)
            last_update_time = current_time

        clock.tick(30)  # Limit frame rate to 30 FPS

    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
