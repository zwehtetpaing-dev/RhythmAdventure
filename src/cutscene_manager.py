# src/cutscene_manager.py
import pygame
from game_object import GameObject

class CutsceneManager(GameObject):
    def __init__(self, hero, triggers):
        self.hero = hero
        self.triggers = triggers
        self.active_scene = None 

    def update(self, keys):
        # Every single frame, we start by assuming the hero is NOT touching a scene
        touching_scene = None
        scene_names = ["A", "B", "C"]
        
        # Check all the invisible tape marks
        for index, trigger_box in enumerate(self.triggers):
            # We still inflate the hitbox slightly so we can sense it while bumping into it
            if self.hero.hitbox.inflate(4, 4).colliderect(trigger_box):
                # We found one! Remember the letter and stop searching.
                touching_scene = scene_names[index]
                break

        # Finally, we update our sticky note. 
        # If the hero stepped away, touching_scene will be None, erasing the note!
        self.active_scene = touching_scene

    def draw(self, screen):
        pass