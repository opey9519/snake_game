# Description: Recreate popular "Snake Game"

import pygame

# Initializes the window
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake')

# Loop to keep game running
run = True

# Position variables
x1 = 300
y1 = 300

# Movement change variables
x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while run:

    # Registering actions with user events
    for event in pygame.event.get(): 
        # when clicking X game closes
        if event.type == pygame.QUIT:
            run = False

        # On keydown press (LEFT, RIGHT, UP, DOWN), x1_change, y1_change variables are altered to allow continous movement during while loop
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    # Changes (x,y) coordinate based on key stroke
    x1 += x1_change
    y1 += y1_change
    # Screen black on refresh
    screen.fill((0,0,0))

    # Creating rectangle with rgb (lime green)
    pygame.draw.rect(screen, (0, 255, 0), [x1,y1,10,10])
    
    # Updates the screen to allow next frame
    pygame.display.update()

    # Sets frames per second to 30
    clock.tick(30)

pygame.quit() # Quits intializer