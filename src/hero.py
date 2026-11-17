import pygame

from .entity import Entity
from .animation import Animator

class Hero(Entity):
    def __init__(self, image_path, start_x, start_y, speed, health, obstacles):
        self.hitbox = pygame.Rect(start_x, start_y, 60, 40)
        # The list of obstacles
        self.obstacles = obstacles
        super().__init__(image_path, start_x, start_y, speed, health)

        # Animation logic
        slime_pictures = [
            "assets/entities/hero/Hero_squeesh.png",  # Flat 
            "assets/entities/hero/Hero_idle.png"   # Tall 
        ]
        self.animator = Animator(frame_paths=slime_pictures, animation_speed=15)
        self.image = self.animator.get_current_image()

    # Move
    def update(self, keys):

        # We start by assuming the slime is standing still
        is_moving = False

        dx = 0
        if keys[pygame.K_a]:
            dx = -self._speed
            is_moving = True
        if keys[pygame.K_d]:
            dx = self._speed
            is_moving = True
            
        # When I hit A and D, dx will change the position of hitbox.
        self.hitbox.x += dx

        # Checking the y-axis screen border
        if self.hitbox.right > 1280:
            self.hitbox.right = 1280
        if self.hitbox.left < 0:
            self.hitbox.left = 0
        
        # Checking obstacle collisions in x axis
        for box in self.obstacles:
            if self.hitbox.colliderect(box):
                if dx > 0:       # Walking right, hit left edge of a wall
                    self.hitbox.right = box.left # 
                elif dx < 0:     # Walking left, hit right edge of a wall
                    self.hitbox.left = box.right

        dy = 0
        if keys[pygame.K_w]:
            dy = -self._speed
            is_moving = True
        if keys[pygame.K_s]:
            dy = self._speed
            is_moving = True
            
        # When I hit W and S, dy will change the position of hitbox.
        self.hitbox.y += dy

        # Checking the y-axis screen border
        if self.hitbox.bottom > 720:
            self.hitbox.bottom = 720
        if self.hitbox.top < 80:
            self.hitbox.top = 80
        
        # Checking obstacle collisions in y axis
        for box in self.obstacles:
            if self.hitbox.colliderect(box):
                if dy > 0:       # Walking down, hit top edge of a wall
                    self.hitbox.bottom = box.top
                elif dy < 0:     # Walking up, hit bottom edge of a wall
                    self.hitbox.top = box.bottom
                    

        # Adjusting character rect model
        self.rect.x = self.hitbox.centerx - 100
        self.rect.y = self.hitbox.centery - 140

        # Activate animation
        self.animator.update(is_moving)
        self.image = self.animator.get_current_image()