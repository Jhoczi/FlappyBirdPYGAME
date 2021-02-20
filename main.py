import pygame, sys, random

# COLORS
WHITE = (0,0,0)
GREEN = (93,240,69)

# GENERAL SETTINGS
screen_width = 1280
screen_height = 860
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Ping Pong')
FPS = 30
run = True

# GRAPHICS
BACKGROUND = pygame.image.load('background.png')
BIRD_IMAGE = pygame.transform.scale(pygame.image.load('bird.png'), (100,70))

# BIRD SETTINGS
bird_x = 150
bird_y = 300
bird_y_change = 0

# OBSTACLES SETTINGS
OBSTACLE_WIDTH = 70
OBSTACLE_HEIGHT = random.randint(250,550)
OBSTACLE_COLOR = GREEN
OBSTACLE_X_CHANGE = -4
obstacle_x = screen_width - 200

# PYGAME INIT
pygame.init()
clock = pygame.time.Clock()

# FUNCTIONS

# BIRD FUNCTION
def DisplayBird(x,y):
    screen.blit(BIRD_IMAGE,(x,y))

# OBSTACLE FUNCTION
def DisplayObstacle(height):
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x, 0, OBSTACLE_WIDTH, height))
    bottom_obstacle_height = 796 - height - 150
    pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle_x,height + 150, OBSTACLE_WIDTH,  bottom_obstacle_height))

# MAIN PROGRAM LOOP
while run:
    # Event control:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = -6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                bird_y_change = 6

    screen.fill(WHITE)
    screen.blit(BACKGROUND, (0,0))

    bird_y += bird_y_change

    if bird_y <= 0:
        bird_y = 0
    if bird_y >= screen_height - BIRD_IMAGE.get_height():
        bird_y = screen_height - BIRD_IMAGE.get_height()

    obstacle_x += OBSTACLE_X_CHANGE
    if obstacle_x <= -10:
        obstacle_x = screen_width - 200
        OBSTACLE_HEIGHT = random.randint(200,400)
    DisplayObstacle(OBSTACLE_HEIGHT)

    DisplayBird(bird_x, bird_y)

    # Updating window:
    pygame.display.update()
    clock.tick(FPS)

# Quit the program
pygame.quit()