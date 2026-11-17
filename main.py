# Example file showing a basic pygame "game loop"
import pygame
from src.hero import Hero
from src.background import Background
from assets.map_data import MAP_COLLISIONS

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


# We read the coordinates from our data file and turn them into pygame.Rect objects.
obstacles = []
for coords in MAP_COLLISIONS["entrance_obstacles"]:
    obstacles.append(pygame.Rect(coords))

cutscenes = []
for coords in MAP_COLLISIONS["entrance_triggers"]:
    cutscenes.append(pygame.Rect(coords))


# Create game objects
hero = Hero("assets/entities/hero/Hero.png", 500, 500, 3, 200, obstacles=obstacles)
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

    # RENDER YOUR GAME HERE ===============================================
    for obj in game_objects:
        obj.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()