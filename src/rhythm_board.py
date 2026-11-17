# src/rhythm_board.py
import pygame
from game_object import GameObject

class RhythmBoard(GameObject):
    def __init__(self):
        self.font = pygame.font.SysFont(None, 40)
        
        # We define the center of each of your 6 lanes (X-coordinates)
        # We leave a slightly larger gap in the middle (between F and J) to separate the left and right hands!
        self.lane_x = [340, 440, 540, 740, 840, 940] 
        
        self.letters = ["S", "D", "F", "J", "K", "L"]
        self.keys = [pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k, pygame.K_l]
        
        # This is the exact Y-coordinate where the player needs to catch the notes
        self.target_y = 600
        
        # A list to remember which keys are currently being held down
        self.pressed = [False] * 6

    def update(self, keys):
        # Every frame, check all 6 keys and update our memory list
        for i in range(6):
            self.pressed[i] = keys[self.keys[i]]

    def draw(self, screen):
        # 1. Draw the faint vertical guidelines for the falling notes
        for x in self.lane_x:
            pygame.draw.line(screen, (50, 45, 45), (x, 0), (x, 720), 2)

        # 2. Draw the catcher's mitts
        for i, x in enumerate(self.lane_x):
            # If the key is pressed, fill the circle with a bright color!
            if self.pressed[i]:
                pygame.draw.circle(screen, (180, 140, 90), (x, self.target_y), 35) # Golden-wood highlight
            
            # Always draw the crisp white outer ring
            pygame.draw.circle(screen, "#F5F5F5", (x, self.target_y), 35, 4)
            
            # 3. Stamp the letter label right below the circle
            text_surface = self.font.render(self.letters[i], True, "#F5F5F5")
            text_rect = text_surface.get_rect(center=(x, self.target_y + 60))
            screen.blit(text_surface, text_rect)