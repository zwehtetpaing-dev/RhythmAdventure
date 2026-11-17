# src/note.py
import pygame
from game_object import GameObject

class Note(GameObject):
    def __init__(self, x_position, target_time):
        self.x = x_position
        self.y = -100  # It starts hidden just above the screen
        
        # The exact millisecond in the song it needs to hit the catcher's mitt
        self.target_time = target_time 
        self.target_y = 600  # Matches the targets in your RhythmBoard!
        
        # Speed: 0.5 pixels per millisecond (meaning it appears about 1.5 seconds before it hits)
        self.speed = 0.5  
        
        # A sticky note to know if the note is still in play, or if it was caught/missed
        self.active = True 

    # Notice we pass 'current_time' instead of 'keys'! 
    # The Note doesn't care about the keyboard, only the music.
    def update(self, current_time):
        if not self.active:
            return

        # 1. How much time is left before we hit the target?
        time_left = self.target_time - current_time
        
        # 2. Physics: Distance = Time * Speed
        distance_to_target = time_left * self.speed
        
        # 3. Place the note exactly that distance above the target
        self.y = self.target_y - distance_to_target
        
        # 4. If the note falls completely off the bottom of the screen, it dies
        if self.y > 750:
            self.active = False

    def draw(self, screen):
        if self.active:
            # Paint the falling note (A nice bright cyan with a white border!)
            pygame.draw.circle(screen, "cyan", (int(self.x), int(self.y)), 30)
            pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), 30, 3)