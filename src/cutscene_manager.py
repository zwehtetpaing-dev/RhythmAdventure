# src/cutscene_manager.py
import pygame
from game_object import GameObject

class CutsceneManager(GameObject):
    def __init__(self, hero, triggers):
        self.hero = hero
        self.triggers = triggers

    def update(self, keys):
        scene_names = ["A", "B", "C"]
        standing_on_mark = False

        for index, trigger_box in enumerate(self.triggers):
            # We inflate the hero's hitbox by 4 pixels (2 on each edge). 
            # This lets them "touch" the trigger while still being blocked by it!
            if self.hero.hitbox.inflate(4, 4).colliderect(trigger_box):
                print(scene_names[index])
                standing_on_mark = True
                
        if not standing_on_mark:
            print("Nope")

    def draw(self, screen):
        pass