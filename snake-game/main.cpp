/*
 * Snake Game in C++ using SDL
 * Dependencies: SDL library, SDL_ttf for text rendering
 */

#include <iostream>
#include <SDL.h>
#include <SDL_ttf.h>
#include <vector>

// Define constants for screen dimensions, grid size, and other game parameters
const int SCREEN_WIDTH = 800;
const int SCREEN_HEIGHT = 600;
const int GRID_SIZE = 20;
const int INITIAL_SNAKE_SIZE = 3;
const int SNAKE_SPEED = 200; // Milliseconds per frame

// Define colors
const SDL_Color BLACK = {0, 0, 0, 255};
const SDL_Color WHITE = {255, 255, 255, 255};

// Define directions for the snake
enum class Direction { UP, DOWN, LEFT, RIGHT };

// Define a structure for representing a snake segment
struct SnakeSegment {
    int x, y;
};

// Function to initialize SDL and create the game window
bool init(SDL_Window*& window, SDL_Renderer*& renderer);

// Function to load game resources (e.g., fonts)
bool loadResources(TTF_Font*& font);

// Function to handle user input
Direction handleInput(Direction currentDirection);

// Function to move the snake
void moveSnake(std::vector<SnakeSegment>& snake, Direction direction);

// Function to check if the snake has collided with the wall or itself
bool checkCollision(const std::vector<SnakeSegment>& snake);

// Function to generate a random position for the food
SDL_Point generateFoodPosition(const std::vector<SnakeSegment>& snake);

int main() {
    SDL_Window* window = nullptr;
    SDL_Renderer* renderer = nullptr;
    TTF_Font* font = nullptr;

    if (!init(window, renderer) || !loadResources(font)) {
        std::cerr << "Initialization failed!" << std::endl;
        return 1;
    }

    // Initialize game variables
    Direction currentDirection = Direction::RIGHT;
    std::vector<SnakeSegment> snake;
    snake.push_back({GRID_SIZE, GRID_SIZE}); // Initialize the snake with a few segments
    SDL_Point food = generateFoodPosition(snake);

    // Game loop
    bool quit = false;
    Uint32 lastUpdateTime = 0;

    while (!quit) {
        Uint32 currentTime = SDL_GetTicks();
        Uint32 elapsedTime = currentTime - lastUpdateTime;

        if (elapsedTime >= SNAKE_SPEED) {
            SDL_Event event;
            while (SDL_PollEvent(&event)) {
                if (event.type == SDL_QUIT) {
                    quit = true;
                }
            }

            currentDirection = handleInput(currentDirection);

            moveSnake(snake, currentDirection);
            if (checkCollision(snake)) {
                quit = true;
            }

            // Check if the snake ate the food
            if (snake[0].x == food.x && snake[0].y == food.y) {
                // Increase the snake's length and generate new food
                snake.push_back({-1, -1});
                food = generateFoodPosition(snake);
            }

            // Clear the screen
            SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
            SDL_RenderClear(renderer);

            // Render the snake
            SDL_SetRenderDrawColor(renderer, 0, 255, 0, 255);
            for (const auto& segment : snake) {
                SDL_Rect segmentRect = {segment.x, segment.y, GRID_SIZE, GRID_SIZE};
                SDL_RenderFillRect(renderer, &segmentRect);
            }

            // Render the food
            SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
            SDL_Rect foodRect = {food.x, food.y, GRID_SIZE, GRID_SIZE};
            SDL_RenderFillRect(renderer, &foodRect);

            // Present the rendered frame
            SDL_RenderPresent(renderer);

            lastUpdateTime = currentTime;
        }
    }

    // Cleanup and exit
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    TTF_CloseFont(font);
    TTF_Quit();
    SDL_Quit();

    return 0;
}

bool init(SDL_Window*& window, SDL_Renderer*& renderer) {
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        std::cerr << "SDL initialization failed: " << SDL_GetError() << std::endl;
        return false;
    }

    if (TTF_Init() < 0) {
        std::cerr << "SDL_ttf initialization failed: " << TTF_GetError() << std::endl;
        SDL_Quit();
        return false;
    }

    window = SDL_CreateWindow("Snake Game", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
                              SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN);
    if (!window) {
        std::cerr << "Window creation failed: " << SDL_GetError() << std::endl;
        TTF_Quit();
        SDL_Quit();
        return false;
    }

    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);
    if (!renderer) {
        std::cerr << "Renderer creation failed: " << SDL_GetError() << std::endl;
        SDL_DestroyWindow(window);
        TTF_Quit();
        SDL_Quit();
        return false;
    }

    return true;
}

bool loadResources(TTF_Font*& font) {
    font = TTF_OpenFont("font.ttf", 24); // Replace with the path to your font file
    if (!font) {
        std::cerr << "Font loading failed: " << TTF_GetError() << std::endl;
        return false;
    }

    return true;
}

Direction handleInput(Direction currentDirection) {
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        if (event.type == SDL_KEYDOWN) {
            switch (event.key.keysym.sym) {
                case SDLK_UP:
                    if (currentDirection != Direction::DOWN) {
                        return Direction::UP;
                    }
                    break;
                case SDLK_DOWN:
                    if (currentDirection != Direction::UP) {
                        return Direction::DOWN;
                    }
                    break;
                case SDLK_LEFT:
                    if (currentDirection != Direction::RIGHT) {
                        return Direction::LEFT;
                    }
                    break;
                case SDLK_RIGHT:
                    if (currentDirection != Direction::LEFT) {
                        return Direction::RIGHT;
                    }
                    break;
            }
        }
    }
    return currentDirection;
}

void moveSnake(std::vector<SnakeSegment>& snake, Direction direction) {
    // Move the snake's body
    for (int i = snake.size() - 1; i > 0; --i) {
        snake[i] = snake[i - 1];
    }

    // Move the snake's head based on the direction
    switch (direction) {
        case Direction::UP:
            snake[0].y -= GRID_SIZE;
            break;
        case Direction::DOWN:
            snake[0].y += GRID_SIZE;
            break;
        case Direction::LEFT:
            snake[0].x -= GRID_SIZE;
            break;
        case Direction::RIGHT:
            snake[0].x += GRID_SIZE;
            break;
    }
}

bool checkCollision(const std::vector<SnakeSegment>& snake) {
    // Check if the snake has collided with the wall
    if (snake[0].x < 0 || snake[0].x >= SCREEN_WIDTH || snake[0].y < 0 || snake[0].y >= SCREEN_HEIGHT) {
        return true;
    }

    // Check if the snake has collided with itself
    for (size_t i = 1; i < snake.size(); ++i) {
        if (snake[i].x == snake[0].x && snake[i].y == snake[0].y) {
            return true;
        }
    }

    return false;
}

SDL_Point generateFoodPosition(const std::vector<SnakeSegment>& snake) {
    SDL_Point foodPosition;
    bool validPosition = false;

    // Keep generating random positions until a valid one is found
    while (!validPosition) {
        foodPosition.x = rand() % (SCREEN_WIDTH / GRID_SIZE) * GRID_SIZE;
        foodPosition.y = rand() % (SCREEN_HEIGHT / GRID_SIZE) * GRID_SIZE;

        // Check if the food is not on the snake's body
        validPosition = true;
        for (const auto& segment : snake) {
            if (foodPosition.x == segment.x && foodPosition.y == segment.y) {
                validPosition = false;
                break;
            }
        }
    }

    return foodPosition;
}
