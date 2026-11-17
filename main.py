# Example file showing a basic pygame "game loop"
import pygame

from src.loader import load_map, load_character
from src.cutscene_manager import CutsceneManager
from src.textbox import TextBox
from src.wasd_overlay import WASDOverlay
from src.menu import MainMenu
from src.rhythm_board import RhythmBoard
from src.rhythm_manager import RhythmManager

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
rhythm_manager = RhythmManager(rhythm_board, "Boss_1")
# ===================================================================================

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check the keys
    keys = pygame.key.get_pressed()
    
    # ================= THE MENU =================
    if keys[pygame.K_ESCAPE]:
        game_state = "MENU"

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
            # 1. Stop the exploration music
            pygame.mixer.music.stop()
            
            # 2. Hand the DJ the boss music and press play! 
            pygame.mixer.music.load("assets/music/Boss_music.mp3")
            pygame.mixer.music.play()
            
            # --- THE FIX: Force the slime to stop squishing! ---
            hero.move_sound.stop()
            hero.is_playing_sound = False
            cutscene_manager.action = None

        screen.fill("black")
        for obj in game_objects:
            obj.draw(screen)

    # ================= RHYTHM BATTLE =================
    elif game_state == "RHYTHM_BATTLE":
        # 1. Update the objects
        rhythm_board.update(keys)
        rhythm_manager.update(keys)  # The brain reads the stopwatch and spawns notes!

        # check if the end of the battle
        if rhythm_manager.is_finished:
            pygame.mixer.music.stop()
            pygame.time.wait(1000)
            game_state = "PLAYING"

        # 2. Erase the old frame
        screen.fill("black")
        
        # 3. Draw the highway first, then draw the notes on top of it!
        rhythm_board.draw(screen)
        rhythm_manager.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()