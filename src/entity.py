import pygame
from game_object import GameObject


class Entity(GameObject):
    def __init__(self, image_path, start_x, start_y, speed, health):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (200, 200)).convert_alpha()
        self.rect = self.image.get_rect(center=(start_x, start_y))

        self._speed = speed
        self._health = health
        self.max_health = health

        # Cache HUD font and scaled portrait so they aren't rebuilt every frame
        self.hud_font = pygame.font.SysFont(None, 28)
        self._cached_portrait_source = self.image
        self._cached_portrait = pygame.transform.scale(self.image, (50, 50))

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = max(0, value)

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, min(self.max_health, value))

    def draw_health_bar(self, screen):
        """Draws the top-left character portrait and HP bar."""
        if self._cached_portrait_source is not self.image:
            self._cached_portrait_source = self.image
            self._cached_portrait = pygame.transform.scale(self.image, (50, 50))

        screen.blit(self._cached_portrait, (20, 20))

        hp_label = self.hud_font.render("HP", True, "white")
        screen.blit(hp_label, (80, 35))

        bar_x, bar_y = 120, 35
        bar_width, bar_height = 200, 20
        health_ratio = self._health / self.max_health if self.max_health > 0 else 0

        bg_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        fill_rect = pygame.Rect(bar_x, bar_y, int(bar_width * health_ratio), bar_height)

        pygame.draw.rect(screen, "red", bg_rect)
        pygame.draw.rect(screen, "green", fill_rect)
        pygame.draw.rect(screen, "#293e2b", bg_rect, 2)

        numbers_label = self.hud_font.render(f"{int(self._health)}", True, "white")
        screen.blit(numbers_label, (bar_x + bar_width + 15, 35))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_health_bar(screen)