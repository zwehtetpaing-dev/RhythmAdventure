import pygame

class Animator:
    def __init__(self, frame_paths, animation_speed):
        # 1. Load and scale all the pictures in the flipbook
        self.frames = []
        for path in frame_paths:
            self.frames.append(self._load_and_scale(path))
            
        # 2. Set up the clocks and page numbers
        self.current_frame = 1           # Start on the tall frame (index 1)
        self.animation_timer = 0         # The stopwatch for our current frame
        self.animation_speed = animation_speed # How high the stopwatch goes before flipping

    def _load_and_scale(self, path):
        """A helper to load the image, scale it to 200x200, and handle transparency."""
        img = pygame.image.load(path)
        img = pygame.transform.scale(img, (200, 200))
        return img.convert_alpha()

    def update(self, is_moving):
        """The math that flips the pages!"""
        if is_moving:
            self.animation_timer += 1
            
            # If the stopwatch hits the limit, flip the page
            if self.animation_timer >= self.animation_speed:
                # This math trick flips 0 to 1, and 1 to 0!
                self.current_frame = 1 - self.current_frame 
                self.animation_timer = 0
        else:
            # When standing still, rest on the tall shape and reset the stopwatch
            self.current_frame = 1
            self.animation_timer = 0

    def get_current_image(self):
        """Hands the correct picture back to the hero."""
        return self.frames[self.current_frame]