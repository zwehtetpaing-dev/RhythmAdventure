# Example file showing a basic pygame "game loop"
import pygame

from src.loader import load_map, load_character

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# ============================ Object creator ====================================
current_room = "Entrance"

# 1. Load the Map
background, obstacles, cutscenes = load_map(current_room)

# 2. Load the Character (and hand them the walls they need to bump into)
hero = load_character(obstacles)

# 3. Pack everything for the polymorphic dispatch loop
game_objects = [background, hero]
# ===================================================================================

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

    # Detecting cut scenes.
    for trigger_box in cutscenes:
        if hero.hitbox.colliderect(trigger_box):
            print("Cutscene detected! The hero is standing on the mark.")
        else:
            print("Nope")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # Draw every object
    for obj in game_objects:
        obj.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()