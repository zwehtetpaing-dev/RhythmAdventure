import pygame
from game_object import GameObject

class Background(GameObject):
    def __init__(self, image_path):
        self.image = pygame.transform.scale(pygame.image.load(image_path), (1280, 720))
        self.image = self.image.convert()

    def update(self, keys):
        pass

    def draw(self, screen):
        screen.blit(self.image, (0, 0))
