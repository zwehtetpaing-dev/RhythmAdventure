# Example file showing a basic pygame "game loop"
import pygame

from src.loader import load_map, load_character
from src.cutscene_manager import CutsceneManager
from src.textbox import TextBox

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# ============================ Object creator ====================================
current_room = "Entrance"

# 1. Load the Map
background, obstacles, cutscenes = load_map(current_room)
all_physical_walls = obstacles + cutscenes

# 2. Load the Character 
hero = load_character(all_physical_walls)

# 3. Hire the Stage Manager (The Brain)
cutscene_manager = CutsceneManager(hero, cutscenes)

# 4. Create the TextBox (The Face), telling it to watch the manager
textbox = TextBox(cutscene_manager)

# 5. Pack everything for the polymorphic dispatch loop
game_objects = [background, hero, cutscene_manager, textbox]
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