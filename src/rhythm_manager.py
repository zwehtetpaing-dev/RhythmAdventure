# src/rhythm_manager.py
import pygame
from game_object import GameObject
from src.note import Note
from assets.beatmap_data import BEATMAP_DATA

class RhythmManager(GameObject):
    def __init__(self, board, song_id):
        self.board = board
        self.combo = 0
        self.font = pygame.font.SysFont(None, 60)
        
        # We load your choreography list
        self.script = BEATMAP_DATA[song_id].copy()
        self.active_notes = []
        
        # --- THE CATCHER'S MITT ---
        # 40 pixels gives you a nice, fair window to hit the note!
        self.hit_margin = 40
        
        # Memory to ensure players actually tap the key, not just hold it down
        self.prev_keys = [False] * 6
        
        # Add these two lines:
        self.click_sound = pygame.mixer.Sound("assets/sound/Click.mp3")
        self.click_sound.set_volume(0.2)

        # Is battle over?
        self.is_finished = False

    def update(self, keys):
        # 1. Ask the DJ what time it is (in milliseconds)
        current_time = pygame.mixer.music.get_pos()
        
        # If the music hasn't started yet, the DJ returns -1. We just wait.
        if current_time < 0:
            return

        # 2. Check the script to see if it's time to spawn a note
        # We look at the first note in the list. If it's less than 2 seconds away, spawn it!
        while len(self.script) > 0 and self.script[0]["time"] - current_time < 2000:
            note_data = self.script.pop(0) # Remove it from the script
            
            # Find the correct X coordinate from the board using the lane number
            lane_idx = note_data["lane"]
            spawn_x = self.board.lane_x[lane_idx]
            
            # Create the note and add it to the stage!
            new_note = Note(spawn_x, note_data["time"])
            self.active_notes.append(new_note)

        # 3. Update all active notes
        for note in self.active_notes:
            note.update(current_time)
            
            # If a note fell completely past the target and died, you missed!
            if not note.active and note.y > 750:
                self.combo = 0 

        # 4. Check for Player Hits 
        for i in range(6):
            key_pressed = keys[self.board.keys[i]]
            key_just_tapped = key_pressed and not self.prev_keys[i]
            
            if key_just_tapped:
                # Add this line right here!
                self.click_sound.play()
                
                # Look for the lowest note in this specific lane
                for note in self.active_notes:
                        
                        # Calculate the distance between the note and the target
                        distance = abs(note.y - self.board.target_y)
                        
                        if distance <= self.hit_margin:
                            # It's a hit! 
                            note.active = False
                            self.combo += 1
                            break # We hit it, stop looking at other notes in this lane
                        else:
                            # They tapped too early or too late!
                            self.combo = 0
                            break

            # Update our key memory for the next frame
            self.prev_keys[i] = key_pressed

        # 5. Clean up dead notes from the computer's memory
        self.active_notes = [note for note in self.active_notes if note.active]


    def draw(self, screen):
        # Draw all the falling notes
        for note in self.active_notes:
            note.draw(screen)

        # If the script is empty AND there are no active notes left falling...
        if len(self.script) == 0 and len(self.active_notes) == 0:
            self.is_finished = True
            
        # Draw the Combo Counter exactly like your sketch
        combo_text = self.font.render(f"Combo: {self.combo}", True, "#F5F5F5")
        combo_rect = combo_text.get_rect(center=(640, 100))
        screen.blit(combo_text, combo_rect)

