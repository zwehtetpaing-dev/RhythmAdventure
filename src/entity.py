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
        """Overrides the Entity health bar to stick to the top-left screen corner."""
        # 1. Make the player's health bar nice and big
        bar_width = 200
        bar_height = 20
        
        # 2. Fix the coordinates to the top-left corner of the screen window
        bar_x = 20
        bar_y = 20
        
        # 3. Calculate the health percentage
        health_ratio = max(0, self._health) / self.max_health
        
        # 4. Create the rectangles using our fixed screen coordinates
        red_rect = pygame.Rect(bar_x, bar_y, bar_width, bar_height)
        green_rect = pygame.Rect(bar_x, bar_y, bar_width * health_ratio, bar_height)
        
        # 5. Draw the tape (Red background, Green health, and a White border)
        pygame.draw.rect(screen, "red", red_rect)
        pygame.draw.rect(screen, "green", green_rect)
        pygame.draw.rect(screen, "#293e2b", red_rect, 3)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.draw_health_bar(screen)
        # Temporary hit box
        # pygame.draw.rect(screen, "blue", self.rect, 2)
        # pygame.draw.rect(screen, "red", self.hitbox, 2)
    