# Description: Recreate popular "Snake Game"

import pygame
import random

# Initializes the window
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')

# Loop to keep game running
run = True

# Position variables
x1 = 300
y1 = 300
x_apple = random.randrange(0, 781)
y_apple = random.randrange(0, 581)
snake_list = []
snake_length = 1

# Function to plot snake parts
def plot_snake(screen, color, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, color, [x, y, 20, 20])
        
# Movement change variables
x1_change = 0
y1_change = 0
direction = 'x' # Directional variable that prohibits opposite direcitonal movement

clock = pygame.time.Clock()

while run:

    # Registering actions with user events
    for event in pygame.event.get(): 
        # when clicking X game closes
        if event.type == pygame.QUIT:
            run = False

        # On keydown press (LEFT, RIGHT, UP, DOWN), x1_change, y1_change variables are altered to allow continous movement during while loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != 'right':
                x1_change = -10
                y1_change = 0
                direction = 'left'
            elif event.key == pygame.K_RIGHT and direction != 'left':
                x1_change = 10
                y1_change = 0
                direction = 'right'
            elif event.key == pygame.K_UP and direction != 'down':
                y1_change = -10
                x1_change = 0
                direction = 'up'
            elif event.key == pygame.K_DOWN and direction != 'up':
                y1_change = 10
                x1_change = 0
                direction = 'down'

    # Changes (x,y) coordinate based on key stroke
    x1 += x1_change
    y1 += y1_change
    
    # If snake hits boundaries game ends
    if x1 <= 0 or x1 >= 800:
        run = False
    elif y1 <= 0 or y1 >= 600:
        run = False
    
    # Screen black on refresh
    screen.fill((0,0,0))

    # Tracks position of head of snake
    head = []
    head.append(x1)
    head.append(y1)
    snake_list.append(head)

    # Creating rectangle with rgb (lime green)
    snake = pygame.draw.rect(screen, (0, 255, 0), [x1, y1, 20, 20])
    apple = pygame.draw.rect(screen, (255,0,0), [x_apple, y_apple, 20, 20])

    if len(snake_list) > snake_length:
        del snake_list[0]

    # Collision statement (if snake collides with apple, respawn apple, append snake)
    if pygame.Rect.colliderect(snake, apple):
        x_apple = random.randrange(0, 781)
        y_apple = random.randrange(0, 581)
        snake_length += 5
        
        apple = pygame.draw.rect(screen, (255,0,0), [x_apple, y_apple, 20, 20])

    # Plots an instance of rectangle based on snake length (incremented by food collision)
    plot_snake(screen, (0, 255, 0), snake_list)
    
    # Updates the screen to allow next frame
    pygame.display.update()

    # Sets frames per second to 20
    clock.tick(20)

pygame.quit() # Quits intializer