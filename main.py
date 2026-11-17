# Example file showing a basic pygame "game loop"
import pygame

from src.loader import load_map, load_character
from src.cutscene_manager import CutsceneManager
from src.textbox import TextBox
from src.wasd_overlay import WASDOverlay
from src.menu import MainMenu
from src.rhythm_board import RhythmBoard

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

# IN GAME
background, obstacles, cutscenes = load_map(current_room)
all_physical_walls = obstacles + cutscenes
hero = load_character(all_physical_walls)
cutscene_manager = CutsceneManager(hero, cutscenes)
textbox = TextBox(cutscene_manager)
wasd_overlay = WASDOverlay()
game_objects = [background, hero, cutscene_manager, textbox, wasd_overlay]

# RHYTHYM BATTLE 
rhythm_board = RhythmBoard()

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

        # Listen for the stage manager's signal to start the boss fight!
        if cutscene_manager.action == "START_RHYTHM":
            game_state = "RHYTHM_BATTLE"

            pygame.mixer.music.stop()
            
            # Erase the signal so it doesn't constantly re-trigger
            cutscene_manager.action = None

        screen.fill("black")
        for obj in game_objects:
            obj.draw(screen)

    # ================= RHYTHM BATTLE =================
    elif game_state == "RHYTHM_BATTLE":
        rhythm_board.update(keys)
        screen.fill("black")
        rhythm_board.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()