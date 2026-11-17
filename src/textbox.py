import pygame
from game_object import GameObject

class TextBox(GameObject):
    def __init__(self, cutscene_manager):
        # We hand the TextBox a reference to the manager so it can peek at its state
        self.cutscene_manager = cutscene_manager
        self.font = pygame.font.SysFont(None, 48)

    def update(self, keys):
        # The TextBox doesn't care about the spacebar anymore. 
        # The manager handles all the key presses for the cutscene!
        pass

    def draw(self, screen):
        # Peek at the manager. Is a cutscene happening?
        scene_letter = self.cutscene_manager.active_scene
        
        if scene_letter:
            # A cutscene is active! Draw the box and the letter.
            box_rect = pygame.Rect(140, 500, 1000, 150)
            
            pygame.draw.rect(screen, "blue", box_rect)
            pygame.draw.rect(screen, "white", box_rect, 4)
            
            text_surface = self.font.render(scene_letter, True, "white")
            screen.blit(text_surface, (160, 520))