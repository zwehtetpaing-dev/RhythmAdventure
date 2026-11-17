# Example file showing a basic pygame "game loop"
import pygame

from src.loader import load_map, load_character
from src.cutscene_manager import CutsceneManager

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# ============================ Object creator ====================================
current_room = "Entrance"

# Load the Map
background, obstacles, cutscenes = load_map(current_room)

# Load the Character (and hand them the walls they need to bump into)
hero = load_character(obstacles)

# Activate cutscene manager
cutscene_manager = CutsceneManager(hero, cutscenes)

# Pack everything for the polymorphic dispatch loop
game_objects = [background, hero, cutscene_manager]
# ===================================================================================

while running:
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

    # Draw every object
    for obj in game_objects:
        obj.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()