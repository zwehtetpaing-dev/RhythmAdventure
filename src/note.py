import pygame
from game_object import GameObject


class Note(GameObject):
    def __init__(self, lane, x_position, target_time):
        self.lane = lane
        self.x = x_position
        self.y = -100
        self.target_time = target_time
        self.target_y = 600
        self.speed = 0.5
        self.active = True
        self.current_time = 0

    def sync_time(self, current_time):
        self.current_time = current_time

    def update(self, keys, events=None):
        if not self.active:
            return

        time_left = self.target_time - self.current_time
        self.y = self.target_y - (time_left * self.speed)

        if self.y > 750:
            self.active = False

    def draw(self, screen):
        if self.active:
            pos = (int(self.x), int(self.y))
            pygame.draw.circle(screen, "cyan", pos, 30)
            pygame.draw.circle(screen, "white", pos, 30, 3)