import pygame

from entity import Entity

class Hero(Entity):
    def __init__(self, image_path, start_x, start_y, speed, health):
        super().__init__(image_path, start_x, start_y, speed, health)

    # Move
    def move(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self._speed  # Up
        if keys[pygame.K_s]:
            self.rect.y += self._speed  # Down
        if keys[pygame.K_a]:
            self.rect.x -= self._speed  # Left
        if keys[pygame.K_d]:
            self.rect.x += self._speed  # Right