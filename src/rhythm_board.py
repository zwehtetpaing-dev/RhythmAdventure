import pygame
from game_object import GameObject


class RhythmBoard(GameObject):
    def __init__(self):
        self.font = pygame.font.SysFont(None, 40)

        self.lane_x = [340, 440, 540, 740, 840, 940]
        self.letters = ["S", "D", "F", "J", "K", "L"]
        self.keys = [pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k, pygame.K_l]
        self.target_y = 600

        self.pressed = [False] * len(self.lane_x)

        # Pre-render static lane letter labels once
        self.letter_labels = []
        for x, letter in zip(self.lane_x, self.letters):
            surf = self.font.render(letter, True, "#F5F5F5")
            rect = surf.get_rect(center=(x, self.target_y + 60))
            self.letter_labels.append((surf, rect))

    def update(self, keys, events=None):
        for i, key in enumerate(self.keys):
            self.pressed[i] = keys[key]

    def draw(self, screen):
        for i, x in enumerate(self.lane_x):
            pygame.draw.line(screen, (50, 45, 45), (x, 0), (x, 720), 2)

            if self.pressed[i]:
                pygame.draw.circle(screen, (180, 140, 90), (x, self.target_y), 35)

            pygame.draw.circle(screen, "#F5F5F5", (x, self.target_y), 35, 4)

            surf, rect = self.letter_labels[i]
            screen.blit(surf, rect)