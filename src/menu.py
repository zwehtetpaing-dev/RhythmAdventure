import pygame
from game_object import GameObject


class MainMenu(GameObject):
    def __init__(self):
        self.title_font = pygame.font.SysFont(None, 120)
        self.option_font = pygame.font.SysFont(None, 60)

        self.options = ["Start Game", "Exit"]
        self.selected_index = 0
        self.action = None

        self.border_color = (180, 140, 90)
        self.bg_color = (40, 35, 35)
        self.highlight_bg = (60, 50, 45)
        self.text_color = "#F5F5F5"

        # Pre-render static title and button text surfaces once
        self.title_surface = self.title_font.render("RHYTHM ADVENTURE", True, self.border_color)
        self.title_rect = self.title_surface.get_rect(center=(640, 200))

        self.rendered_options = [
            (
                self.option_font.render(opt, True, self.text_color),
                self.option_font.render(f">  {opt}  <", True, self.text_color),
            )
            for opt in self.options
        ]
        self.button_rects = [
            pygame.Rect(0, 0, 400, 80).move(640 - 200, 400 + (i * 120) - 40)
            for i in range(len(self.options))
        ]

    def reset(self):
        self.action = None
        self.selected_index = 0

    def update(self, keys, events=None):
        if not events:
            return

        for event in events:
            if event.type != pygame.KEYDOWN:
                continue

            if event.key in (pygame.K_w, pygame.K_UP):
                self.selected_index = (self.selected_index - 1) % len(self.options)
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                self.selected_index = (self.selected_index + 1) % len(self.options)
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                self.action = "START" if self.selected_index == 0 else "EXIT"

    def draw(self, screen):
        screen.fill((20, 20, 20))
        screen.blit(self.title_surface, self.title_rect)

        for i, button_rect in enumerate(self.button_rects):
            is_selected = i == self.selected_index
            current_bg = self.highlight_bg if is_selected else self.bg_color
            text_surface = self.rendered_options[i][1 if is_selected else 0]

            pygame.draw.rect(screen, current_bg, button_rect)
            pygame.draw.rect(screen, self.border_color, button_rect, 4)
            screen.blit(text_surface, text_surface.get_rect(center=button_rect.center))