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
        self.max_health = health

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


    # Health bar creation
    def draw_health_bar(self, screen):
        """Overrides the Entity health bar to draw a full UI dashboard."""
        
        # 1. THE PORTRAIT
        # We take whatever picture the slime is currently using, shrink a copy to 50x50, 
        # and stick it in the top left corner.
        portrait = pygame.transform.scale(self.image, (50, 50))
        screen.blit(portrait, (20, 20))
        
        # 2. THE LABEL MAKER (Font setup)
        # We tell Pygame to grab a default system font, size 28.
        font = pygame.font.SysFont(None, 28)
        
        # 3. THE "HP" TEXT
        # We print "HP" onto a transparent sticker in white ink, and place it next to the portrait.
        hp_sticker = font.render("HP", True, "white")
        screen.blit(hp_sticker, (80, 35))
        
        # 4. THE HEALTH TAPE
        bar_x = 120
        bar_y = 35
        bar_width = 200
        bar_height = 20
        
        health_ratio = max(0, self._health) / self.max_health
        
        red_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        green_rect = pygame.Rect(bar_x, bar_y, bar_width * health_ratio, bar_height)
        
        pygame.draw.rect(screen, "red", red_rect)
        pygame.draw.rect(screen, "green", green_rect)
        pygame.draw.rect(screen, "#293e2b", red_rect, 2) # A crisp 2-pixel white border
        
        # 5. THE HEALTH NUMBERS
        # We print the exact numbers (like "50 / 100") onto another sticker, 
        # and place it right after the end of the health bar.
        health_text = f"{int(self._health)}"
        numbers_sticker = font.render(health_text, True, "white")
        screen.blit(numbers_sticker, (bar_x + bar_width + 15, 35))

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_health_bar(screen)
        # Temporary hit box
        # pygame.draw.rect(screen, "blue", self.rect, 2)
        # pygame.draw.rect(screen, "red", self.hitbox, 2)
    