# src/menu.py
import pygame
from game_object import GameObject

class MainMenu(GameObject):
    def __init__(self):
        self.title_font = pygame.font.SysFont(None, 120)
        self.option_font = pygame.font.SysFont(None, 80)
        
        self.options = ["Start Game", "Exit"]
        self.selected_index = 0  # 0 is Start, 1 is Exit
        self.action = None       # Our sticky note for main.py
        
        # Memory flags to prevent the menu from flying too fast
        self.w_was_pressed = False
        self.s_was_pressed = False

    def update(self, keys):
        # --- Handle W (Move Up) ---
        if keys[pygame.K_w]:
            if not self.w_was_pressed:
                # Move up, and if we go above 0, wrap around to the bottom!
                self.selected_index -= 1
                if self.selected_index < 0:
                    self.selected_index = len(self.options) - 1
            self.w_was_pressed = True
        else:
            self.w_was_pressed = False
            
        # --- Handle S (Move Down) ---
        if keys[pygame.K_s]:
            if not self.s_was_pressed:
                # Move down, and if we go past the bottom, wrap around to 0!
                self.selected_index += 1
                if self.selected_index >= len(self.options):
                    self.selected_index = 0
            self.s_was_pressed = True
        else:
            self.s_was_pressed = False
            
        # --- Handle Spacebar (Select) ---
        if keys[pygame.K_SPACE]:
            if self.selected_index == 0:
                self.action = "START"
            elif self.selected_index == 1:
                self.action = "EXIT"

    def draw(self, screen):
        screen.fill("black")
        
        # Draw the Title perfectly centered
        # (Since your screen is 1280 wide, x=640 is the exact center)
        title_surface = self.title_font.render("RHYTHM ADVENTURE", True, "white")
        title_rect = title_surface.get_rect(center=(640, 200))
        screen.blit(title_surface, title_rect)
        
        # Draw the Options
        for index, option_text in enumerate(self.options):
            # If this is the selected option, make it green and put arrows around it!
            if index == self.selected_index:
                color = "green"
                display_text = f"> {option_text} <"
            else:
                color = "white"
                display_text = option_text
                
            text_surface = self.option_font.render(display_text, True, color)
            
            # We stack them vertically by pushing the Y coordinate down based on the index
            text_rect = text_surface.get_rect(center=(640, 400 + (index * 100)))
            screen.blit(text_surface, text_rect)