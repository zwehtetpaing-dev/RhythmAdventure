# src/textbox.py
import pygame
from game_object import GameObject

class TextBox(GameObject):
    def __init__(self, cutscene_manager):
        self.cutscene_manager = cutscene_manager
        
        # We set up two different font sizes: a small one for the name, a large one for the text
        self.name_font = pygame.font.SysFont(None, 32)
        self.dialog_font = pygame.font.SysFont(None, 48)
        
        # This is our script! It translates the A, B, C signals from the manager 
        # into actual names and environmental lore.
        self.dialogues = {
            "A": {"name": "???", "text": "Beware the slimes ahead..."},
            "B": {"name": "???", "text": "Only those with rhythm may pass."},
            "C": {"name": "???", "text": "The Boss Room lies beyond this point!"}
        }

    def update(self, keys):
        pass

    def draw(self, screen):
        # Peek at the manager's sticky note
        scene_id = self.cutscene_manager.active_scene
        
        # If the manager is seeing a scene, and we have a script for it, draw the boxes!
        if scene_id and scene_id in self.dialogues:
            content = self.dialogues[scene_id]
            
            # --- COLOR PALETTE ---
            bg_color = (40, 35, 35)       # A dark earthy brown/grey for the background
            border_color = (180, 140, 90) # A golden-wood color for the frame
            name_bg = (60, 50, 45)        # Slightly lighter brown for the name tag
            text_color = "#F5F5F5"        # Soft Pearl off-white to prevent eye fatigue
            
            # --- 1. THE MAIN DIALOGUE BOX ---
            # We place this near the bottom of the screen (y=540)
            main_rect = pygame.Rect(140, 540, 1000, 140)
            pygame.draw.rect(screen, bg_color, main_rect)
            pygame.draw.rect(screen, border_color, main_rect, 4) 
            
            # --- 2. THE NAME TAG BOX ---
            # We place this right on top of the main box (y=500), aligned to the left
            name_rect = pygame.Rect(140, 500, 240, 40)
            pygame.draw.rect(screen, name_bg, name_rect)
            pygame.draw.rect(screen, border_color, name_rect, 4)
            
            # --- 3. PAINTING THE WORDS ---
            # Render the Name (colored to match the border for a cohesive UI look)
            name_surface = self.name_font.render(content["name"], True, border_color)
            screen.blit(name_surface, (name_rect.x + 15, name_rect.y + 10))
            
            # Render the Dialogue (using your preferred soft off-white)
            text_surface = self.dialog_font.render(content["text"], True, text_color)
            screen.blit(text_surface, (main_rect.x + 30, main_rect.y + 30))