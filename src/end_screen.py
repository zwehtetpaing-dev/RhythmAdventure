import pygame
from game_object import GameObject


class EndScreen(GameObject):
    """Displays Victory or Game Over results and handles full game restart."""

    def __init__(self):
        self.title_font = pygame.font.SysFont(None, 110)
        self.stat_font = pygame.font.SysFont(None, 46)
        self.hint_font = pygame.font.SysFont(None, 36)

        self.action = None
        self._surfaces = []

    def configure(self, outcome, score, max_combo, accuracy):
        self.action = None
        is_victory = outcome == "VICTORY"

        title_text = "VICTORY!" if is_victory else "GAME OVER"
        title_color = (180, 140, 90) if is_victory else (210, 65, 65)

        lines = [
            (self.title_font, title_text, title_color, 180),
            (self.stat_font, f"Final Score: {score}", "#F5F5F5", 310),
            (self.stat_font, f"Max Combo: {max_combo}", "#F5F5F5", 370),
            (self.stat_font, f"Accuracy: {accuracy:.1f}%", "#F5F5F5", 430),
            (self.hint_font, "[R / SPACE] Restart Game     |     [ESC] Main Menu", (180, 140, 90), 560),
        ]

        self._surfaces = []
        for font, text, color, y_pos in lines:
            surf = font.render(text, True, color)
            rect = surf.get_rect(center=(640, y_pos))
            self._surfaces.append((surf, rect))

    def update(self, keys, events=None):
        if not events:
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_r, pygame.K_SPACE, pygame.K_RETURN):
                    self.action = "RESTART"

    def draw(self, screen):
        screen.fill((20, 20, 20))

        card_rect = pygame.Rect(0, 0, 760, 480)
        card_rect.center = (640, 360)
        pygame.draw.rect(screen, (40, 35, 35), card_rect)
        pygame.draw.rect(screen, (180, 140, 90), card_rect, 4)

        for surf, rect in self._surfaces:
            screen.blit(surf, rect)