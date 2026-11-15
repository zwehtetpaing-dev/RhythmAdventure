import pygame

# 1. Initialize Pygame and window
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Undertale-Style RPG")
clock = pygame.time.Clock()

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GRAY = (120, 120, 120)

# Fonts (SysFont automatically falls back if Courier isn't installed)
title_font = pygame.font.SysFont("couriernew", 52, bold=True)
menu_font = pygame.font.SysFont("couriernew", 28, bold=True)
note_font = pygame.font.SysFont("couriernew", 18)

# Menu setup
options = ["Start", "Continue", "Exit"]
selected_index = 0
has_save_file = False  # Toggle this to True later when we build saving!
status_message = ""
state = "TITLE"  # Tracks whether we are on the title screen or in-game


def draw_soul(surface, x, y):
    """Draws a 16x16 red Soul heart using basic shapes (no image file needed)."""
    pygame.draw.circle(surface, RED, (x + 4, y + 5), 4)
    pygame.draw.circle(surface, RED, (x + 12, y + 5), 4)
    pygame.draw.polygon(surface, RED, [(x, y + 6), (x + 16, y + 6), (x + 8, y + 15)])


running = True
while running:
    clock.tick(60)

    # 2. Handle Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if state == "TITLE":
                # Move cursor up/down and wrap around using modulo (%)
                if event.key in (pygame.K_UP, pygame.K_w):
                    selected_index = (selected_index - 1) % len(options)
                    status_message = ""
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    selected_index = (selected_index + 1) % len(options)
                    status_message = ""

                # Confirm selection (Enter or Z)
                elif event.key in (pygame.K_RETURN, pygame.K_z):
                    choice = options[selected_index]
                    if choice == "Start":
                        state = "GAME"
                    elif choice == "Continue":
                        if has_save_file:
                            state = "GAME"
                        else:
                            status_message = "* No save file found."
                    elif choice == "Exit":
                        running = False

            elif state == "GAME":
                # Press Escape to return to the title screen for testing
                if event.key == pygame.K_ESCAPE:
                    state = "TITLE"

    # 3. Draw Everything
    screen.fill(BLACK)

    if state == "TITLE":
        # Draw Game Title
        title_surf = title_font.render("UNDERTALE-ISH", True, WHITE)
        title_rect = title_surf.get_rect(center=(WIDTH // 2, 110))
        screen.blit(title_surf, title_rect)

        # Draw Menu Options
        start_y = 230
        spacing = 50
        for i, option in enumerate(options):
            is_selected = (i == selected_index)

            # Gray out "Continue" if there's no save file, otherwise highlight yellow
            if option == "Continue" and not has_save_file:
                color = YELLOW if is_selected else GRAY
            else:
                color = YELLOW if is_selected else WHITE

            text_surf = menu_font.render(option, True, color)
            text_rect = text_surf.get_rect(center=(WIDTH // 2, start_y + i * spacing))
            screen.blit(text_surf, text_rect)

            # Draw the red Soul heart just to the left of the active option
            if is_selected:
                draw_soul(screen, text_rect.left - 30, text_rect.centery - 8)

        # Draw feedback message (e.g., "* No save file found.")
        if status_message:
            msg_surf = note_font.render(status_message, True, WHITE)
            msg_rect = msg_surf.get_rect(center=(WIDTH // 2, 410))
            screen.blit(msg_surf, msg_rect)

        # Controls hint at the bottom
        hint_surf = note_font.render("[Arrows/WASD] Move   [Z / Enter] Select", True, GRAY)
        screen.blit(hint_surf, hint_surf.get_rect(center=(WIDTH // 2, 450)))

    elif state == "GAME":
        game_surf = menu_font.render("* Your journey begins...", True, WHITE)
        back_surf = note_font.render("(Press ESC to go back to Title)", True, GRAY)
        screen.blit(game_surf, game_surf.get_rect(center=(WIDTH // 2, 220)))
        screen.blit(back_surf, back_surf.get_rect(center=(WIDTH // 2, 270)))

    pygame.display.flip()

pygame.quit()