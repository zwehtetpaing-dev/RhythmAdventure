# Example file showing a basic pygame "game loop"
import pygame
from render.hero import Hero
from render.background import Background

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# Create game objects
hero = Hero("assets/entities/hero/Hero.png", 100, 100, 3, 100)
background = Background("assets/background/Entrance.png")

# Unified polymorphic dispatch
game_objects = [background, hero]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # CHECK THE KEYS
    keys = pygame.key.get_pressed()
    
    # Update every object
    for obj in game_objects:
        obj.update(keys)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for obj in game_objects:
        obj.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()