import pygame
from game_object import GameObject

class WASDOverlay(GameObject):
    def __init__(self):
        # We shrink the font size to 28 to fit the new smaller buttons
        self.font = pygame.font.SysFont(None, 28)
        
        # We shrink the boxes to 35x35 and push them deep into the bottom-left corner
        # (Screen height is 720, so placing them at 630 and 670 puts them right at the bottom)
        self.btn_w = pygame.Rect(55, 630, 35, 35)
        self.btn_a = pygame.Rect(15, 670, 35, 35)
        self.btn_s = pygame.Rect(55, 670, 35, 35)
        self.btn_d = pygame.Rect(95, 670, 35, 35)
        
        self.w_pressed = False
        self.a_pressed = False
        self.s_pressed = False
        self.d_pressed = False
    def update(self, keys):
        # We look at the keyboard and update our internal sticky notes
        self.w_pressed = keys[pygame.K_w]
        self.a_pressed = keys[pygame.K_a]
        self.s_pressed = keys[pygame.K_s]
        self.d_pressed = keys[pygame.K_d]

    def _draw_button(self, screen, rect, letter, is_pressed):
        """A small helper function to paint a single button."""
        
        # If pressed, the button glows bright green. If not, it sleeps in a dim grey.
        bg_color = "green" if is_pressed else (60, 60, 60)
        text_color = "black" if is_pressed else "white"
        
        # Draw the button background and a crisp white border
        pygame.draw.rect(screen, bg_color, rect)
        pygame.draw.rect(screen, "white", rect, 3)
        
        # Stamp the letter perfectly in the center of the box
        text_surface = self.font.render(letter, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        screen.blit(text_surface, text_rect)

    def draw(self, screen):
        # Paint all four buttons using our helper function
        self._draw_button(screen, self.btn_w, "W", self.w_pressed)
        self._draw_button(screen, self.btn_a, "A", self.a_pressed)
        self._draw_button(screen, self.btn_s, "S", self.s_pressed)
        self._draw_button(screen, self.btn_d, "D", self.d_pressed)