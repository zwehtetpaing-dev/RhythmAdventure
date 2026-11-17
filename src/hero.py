import pygame
from .entity import Entity
from .animation import Animator


class Hero(Entity):
    def __init__(self, image_path, start_x, start_y, speed, health, obstacles):
        self.hitbox = pygame.Rect(start_x, start_y, 60, 40)
        self.obstacles = obstacles
        self.walk_bounds = pygame.Rect(0, 80, 1280, 640)
        super().__init__(image_path, start_x, start_y, speed, health)

        slime_pictures = [
            "assets/entities/hero/Hero_squeesh.png",
            "assets/entities/hero/Hero_idle.png",
        ]
        self.animator = Animator(frame_paths=slime_pictures, animation_speed=15)
        self.image = self.animator.get_current_image()

        self.move_sound = pygame.mixer.Sound("assets/sound/Slime_Move.mp3")
        self.move_sound.set_volume(0.3)
        self.is_playing_sound = False

    def stop_sound(self):
        if self.is_playing_sound:
            self.move_sound.stop()
            self.is_playing_sound = False

    def _update_sound(self, is_moving):
        if is_moving and not self.is_playing_sound:
            self.move_sound.play(-1)
            self.is_playing_sound = True
        elif not is_moving and self.is_playing_sound:
            self.stop_sound()

    def update(self, keys, events=None):
        direction = pygame.math.Vector2(
            keys[pygame.K_d] - keys[pygame.K_a],
            keys[pygame.K_s] - keys[pygame.K_w],
        )

        is_moving = direction.length_squared() > 0
        if is_moving:
            direction = direction.normalize() * self._speed

        # Move & resolve collisions on X axis
        self.hitbox.x += round(direction.x)
        for box in self.obstacles:
            if self.hitbox.colliderect(box):
                if direction.x > 0:
                    self.hitbox.right = box.left
                elif direction.x < 0:
                    self.hitbox.left = box.right

        # Move & resolve collisions on Y axis
        self.hitbox.y += round(direction.y)
        for box in self.obstacles:
            if self.hitbox.colliderect(box):
                if direction.y > 0:
                    self.hitbox.bottom = box.top
                elif direction.y < 0:
                    self.hitbox.top = box.bottom

        # Keep hero inside the playable screen area
        self.hitbox.clamp_ip(self.walk_bounds)

        # Sync sprite rect with hitbox
        self.rect.x = self.hitbox.centerx - 100
        self.rect.y = self.hitbox.centery - 140

        self.animator.update(is_moving)
        self.image = self.animator.get_current_image()
        self._update_sound(is_moving)