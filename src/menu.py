# src/menu.py
import pygame
from game_object import GameObject

class MainMenu(GameObject):
    def __init__(self):
        self.title_font = pygame.font.SysFont(None, 120)
        self.option_font = pygame.font.SysFont(None, 60)
        
        self.options = ["Start Game", "Exit"]
        self.selected_index = 0  
        self.action = None       
        
        self.w_was_pressed = False
        self.s_was_pressed = False

    def update(self, keys):
        # --- Handle W (Move Up) ---
        if keys[pygame.K_w]:
            if not self.w_was_pressed:
                self.selected_index -= 1
                if self.selected_index < 0:
                    self.selected_index = len(self.options) - 1
            self.w_was_pressed = True
        else:
            self.w_was_pressed = False
            
        # --- Handle S (Move Down) ---
        if keys[pygame.K_s]:
            if not self.s_was_pressed:
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
        # A dark charcoal background so the earthy UI boxes pop
        screen.fill((20, 20, 20))
        
        # --- COLOR PALETTE (Matched to your TextBox) ---
        border_color = (180, 140, 90) # Golden-wood
        bg_color = (40, 35, 35)       # Dark earthy brown
        highlight_bg = (60, 50, 45)   # Lighter brown for the selected button
        text_color = "#F5F5F5"        # Soft Pearl off-white
        
        # --- DRAW THE TITLE ---
        # We paint the title in the golden-wood color to tie the room together
        title_surface = self.title_font.render("RHYTHM ADVENTURE", True, border_color)
        title_rect = title_surface.get_rect(center=(640, 200))
        screen.blit(title_surface, title_rect)
        
        # --- DRAW THE UI BUTTONS ---
        for index, option_text in enumerate(self.options):
            
            # Determine the box color and text based on whether it is currently selected
            if index == self.selected_index:
                current_bg = highlight_bg
                display_text = f">  {option_text}  <"
            else:
                current_bg = bg_color
                display_text = option_text
                
            # 1. Math out the box dimensions
            # We make each button 400px wide and 80px tall
            button_rect = pygame.Rect(0, 0, 400, 80)
            # Center it horizontally, and push it down 120px for each index
            button_rect.center = (640, 400 + (index * 120))
            
            # 2. Paint the wooden box
            pygame.draw.rect(screen, current_bg, button_rect)
            pygame.draw.rect(screen, border_color, button_rect, 4)
            
            # 3. Stamp the soft pearl text perfectly in the middle of the box
            text_surface = self.option_font.render(display_text, True, text_color)
            text_rect = text_surface.get_rect(center=button_rect.center)
            screen.blit(text_surface, text_rect)