import pygame
from game_object import GameObject

class Entity(GameObject):
    def __init__ (self, image_path, start_x, start_y, speed, health):
        # Load the image and transform the scale to 200 x 200
        self.image = pygame.transform.scale(pygame.image.load(image_path), (200,200))
        # Make the image transparent
        self.image = self.image.convert_alpha()
        # Create a invisible rect that is same size as self.image
        self.rect = self.image.get_rect()
        # Positioning the rect
        self.rect.center = (start_x, start_y)

        self._speed = speed
        self._health = health

    # Speed
    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        if value != self._speed:
            value = self._speed 

    # Health
    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        if value < 0:
            self._health = 0
        else:
            self._health = value


    def draw(self, screen):
        screen.blit(self.image, self.rect)

        # Temporary hit box
        # pygame.draw.rect(screen, "blue", self.rect, 2)
        # pygame.draw.rect(screen, "red", self.hitbox, 2)
    