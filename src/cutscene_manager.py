# src/cutscene_manager.py
import pygame
from game_object import GameObject

class CutsceneManager(GameObject):
    def __init__(self, hero, triggers):
        self.hero = hero
        self.triggers = triggers
        self.active_scene = None 
        self.action = None

    def update(self, keys):
        # 1. Always check where the hero is standing, no matter what
        touching_scene = None
        scene_names = ["A", "B", "C"]
        
        for index, trigger_box in enumerate(self.triggers):
            if self.hero.hitbox.inflate(4, 4).colliderect(trigger_box):
                touching_scene = scene_names[index]
                break

        # Update our sticky note
        self.active_scene = touching_scene

        # 2. If they are touching A AND they press space, trigger the door!
        if self.active_scene == "A" and keys[pygame.K_SPACE]:
            print("Transitioning to Rhythm Mode...")
            self.action = "START_RHYTHM"
            # Push them back slightly just to prove the button press registered!
            # self.hero.hitbox.y += 10

    def draw(self, screen):
        pass