# src/cutscene_manager.py
import pygame
from game_object import GameObject

class CutsceneManager(GameObject):
    def __init__(self, hero, triggers):
        # The manager just needs to watch the hero and the invisible tape marks
        self.hero = hero
        self.triggers = triggers

    def update(self, keys):
        # The manager silently watches all the invisible tape marks
        for trigger_box in self.triggers:
            if self.hero.hitbox.colliderect(trigger_box):
                print("Cutscene detected! The hero is standing on the mark.")
            else:
                print("Nope")

    def draw(self, screen):
        # It doesn't need to draw anything yet, so we just pass!
        pass