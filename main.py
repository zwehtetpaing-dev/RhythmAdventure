# Example file showing a basic pygame "game loop"
import pygame

from src.loader import load_map, load_character
from src.cutscene_manager import CutsceneManager
from src.textbox import TextBox
from src.wasd_overlay import WASDOverlay
from src.menu import MainMenu

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# ============================ Object creator ====================================
# Menu
main_menu = MainMenu()
game_state = "MENU"  # The game starts in the lobby!

current_room = "Entrance"

# Load the Map
background, obstacles, cutscenes = load_map(current_room)
all_physical_walls = obstacles + cutscenes

# Load the Character 
hero = load_character(all_physical_walls)

# Hire the Stage Manager (The Brain)
cutscene_manager = CutsceneManager(hero, cutscenes)

# Create the TextBox (The Face), telling it to watch the manager
textbox = TextBox(cutscene_manager)

# WASD UI overlay
wasd_overlay = WASDOverlay()

# Pack everything for the polymorphic dispatch loop
game_objects = [background, hero, cutscene_manager, textbox, wasd_overlay]
# ===================================================================================

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check the keys
    keys = pygame.key.get_pressed()
    
    # ================= THE MENU =================
    if game_state == "MENU":
        main_menu.update(keys)
        main_menu.draw(screen)
        
        # Listen for the menu's action signal
        if main_menu.action == "START":
            game_state = "PLAYING" # Open the curtains!
        elif main_menu.action == "EXIT":
            running = False        # Close the window!
            
    # ================= IN GAME =================
    elif game_state == "PLAYING":
        for obj in game_objects:
            obj.update(keys)

        screen.fill("black")

        for obj in game_objects:
            obj.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()