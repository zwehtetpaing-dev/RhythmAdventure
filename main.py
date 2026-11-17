import pygame

from src.loader import load_map, load_character, play_room_music
from src.cutscene_manager import CutsceneManager
from src.textbox import TextBox
from src.wasd_overlay import WASDOverlay
from src.menu import MainMenu
from src.rhythm_board import RhythmBoard
from src.rhythm_manager import RhythmManager
from src.end_screen import EndScreen

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Rhythm Adventure")
clock = pygame.time.Clock()
running = True

# ============================ Object Setup ====================================
main_menu = MainMenu()
end_screen = EndScreen()
game_state = "MENU"
current_room = "Entrance"

# Overworld objects
background, obstacles, cutscenes = load_map(current_room)
all_physical_walls = obstacles + cutscenes
hero = load_character(all_physical_walls)
cutscene_manager = CutsceneManager(hero, cutscenes)
textbox = TextBox(cutscene_manager)
wasd_overlay = WASDOverlay()
game_objects = [background, hero, cutscene_manager, textbox, wasd_overlay]

# Rhythm battle objects
rhythm_board = RhythmBoard()
rhythm_manager = None
battle_objects = []


def reset_game():
    """Restores hero health, position, and room state for a fresh run."""
    hero.stop_sound()
    hero.health = hero.max_health
    hero.hitbox.topleft = (500, 500)
    hero.rect.center = (500, 500)
    cutscene_manager.action = None
    play_room_music(current_room)
# ==============================================================================


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if game_state in ("PLAYING", "RHYTHM_BATTLE", "VICTORY", "GAME_OVER"):
                hero.stop_sound()
                pygame.mixer.music.stop()
                main_menu.reset()
                game_state = "MENU"

    keys = pygame.key.get_pressed()

    # ================= THE MENU =================
    if game_state == "MENU":
        main_menu.update(keys, events)
        main_menu.draw(screen)

        if main_menu.action == "START":
            main_menu.reset()
            reset_game()
            game_state = "PLAYING"
        elif main_menu.action == "EXIT":
            running = False

    # ================= IN GAME =================
    elif game_state == "PLAYING":
        for obj in game_objects:
            obj.update(keys)

        if cutscene_manager.action == "START_RHYTHM":
            cutscene_manager.action = None
            hero.stop_sound()

            rhythm_manager = RhythmManager(rhythm_board, hero, "Boss_1")
            battle_objects = [rhythm_board, rhythm_manager]
            game_state = "RHYTHM_BATTLE"

            pygame.mixer.music.stop()
            pygame.mixer.music.load("assets/music/Boss_music.mp3")
            pygame.mixer.music.play()

        screen.fill("black")
        for obj in game_objects:
            obj.draw(screen)

    # ================= RHYTHM BATTLE =================
    elif game_state == "RHYTHM_BATTLE":
        for obj in battle_objects:
            obj.update(keys, events)

        if hero.health <= 0:
            pygame.mixer.music.stop()
            end_screen.configure(
                "GAME_OVER",
                rhythm_manager.score,
                rhythm_manager.max_combo,
                rhythm_manager.accuracy,
            )
            game_state = "GAME_OVER"
        elif rhythm_manager.is_finished:
            pygame.mixer.music.stop()
            end_screen.configure(
                "VICTORY",
                rhythm_manager.score,
                rhythm_manager.max_combo,
                rhythm_manager.accuracy,
            )
            game_state = "VICTORY"

        screen.fill("black")
        for obj in battle_objects:
            obj.draw(screen)

    # ================= END SCREENS =================
    elif game_state in ("VICTORY", "GAME_OVER"):
        end_screen.update(keys, events)
        end_screen.draw(screen)

        if end_screen.action == "RESTART":
            reset_game()
            game_state = "PLAYING"

    pygame.display.flip()
    clock.tick(60)

pygame.quit()