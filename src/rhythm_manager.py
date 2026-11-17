import pygame
from game_object import GameObject
from src.note import Note
from assets.beatmap_data import BEATMAP_DATA


class RhythmManager(GameObject):
    def __init__(self, board, hero, song_id, miss_damage=20):
        self.board = board
        self.hero = hero
        self.miss_damage = miss_damage
        self.font = pygame.font.SysFont(None, 48)

        self.script = BEATMAP_DATA[song_id].copy()
        self.active_notes = []
        self.hit_margin = 40

        self.key_to_lane = {key: i for i, key in enumerate(self.board.keys)}

        self.click_sound = pygame.mixer.Sound("assets/sound/Click.mp3")
        self.click_sound.set_volume(0.2)

        # Encapsulated stats & cached HUD surfaces
        self._score = 0
        self.combo = 0
        self.max_combo = 0
        self.hits = 0
        self.misses = 0

        self._cached_hud_state = None
        self._hud_surface = None
        self._hud_rect = None

        # Song clock & non-blocking finish state (60 frames = 1 second at 60 FPS)
        self._has_started = False
        self._last_time = 0
        self._is_finished = False
        self._finish_timer = 0
        self._finish_delay_frames = 60

    @property
    def score(self):
        return self._score

    @property
    def accuracy(self):
        total = self.hits + self.misses
        return (self.hits / total) * 100.0 if total > 0 else 100.0

    @property
    def is_finished(self):
        return self._is_finished

    def _register_miss(self):
        self.combo = 0
        self.misses += 1
        self.hero.health -= self.miss_damage

    def _handle_lane_tap(self, lane_idx):
        self.click_sound.play()

        lane_notes = [n for n in self.active_notes if n.active and n.lane == lane_idx]
        if not lane_notes:
            self._register_miss()
            return

        closest_note = max(lane_notes, key=lambda n: n.y)
        if abs(closest_note.y - self.board.target_y) <= self.hit_margin:
            closest_note.active = False
            self.hits += 1
            self.combo += 1
            self._score += 100 + (self.combo * 10)
            if self.combo > self.max_combo:
                self.max_combo = self.combo
        else:
            self._register_miss()

    def update(self, keys, events=None):
        current_time = pygame.mixer.music.get_pos()
        if current_time >= 0:
            self._has_started = True
            self._last_time = current_time
        elif self._has_started:
            self._last_time += 1000 / 60
            current_time = self._last_time
        else:
            return

        # 1. Spawn notes arriving within the next 2000ms
        while self.script and self.script[0]["time"] - current_time < 2000:
            note_data = self.script.pop(0)
            lane_idx = note_data["lane"]
            spawn_x = self.board.lane_x[lane_idx]
            self.active_notes.append(Note(lane_idx, spawn_x, note_data["time"]))

        # 2. Update active notes polymorphically and penalize missed notes
        for note in self.active_notes:
            note.sync_time(current_time)
            note.update(keys, events)
            if not note.active and note.y > 750:
                self._register_miss()

        # 3. Process single-frame key taps
        if events:
            for event in events:
                if event.type == pygame.KEYDOWN and event.key in self.key_to_lane:
                    self._handle_lane_tap(self.key_to_lane[event.key])

        # 4. Clean up inactive notes
        self.active_notes = [note for note in self.active_notes if note.active]

        # 5. Non-blocking end-of-song transition timer
        if not self.script and not self.active_notes:
            self._finish_timer += 1
            if self._finish_timer >= self._finish_delay_frames:
                self._is_finished = True

    def draw(self, screen):
        for note in self.active_notes:
            note.draw(screen)

        # Show the Hero's HP bar in the top-left during combat
        self.hero.draw_health_bar(screen)

        hud_state = (self._score, self.combo, self.misses)
        if hud_state != self._cached_hud_state:
            self._cached_hud_state = hud_state
            hud_text = f"Score: {self._score}   |   Combo: {self.combo}   |   Acc: {self.accuracy:.0f}%"
            self._hud_surface = self.font.render(hud_text, True, "#F5F5F5")
            self._hud_rect = self._hud_surface.get_rect(center=(640, 105))

        screen.blit(self._hud_surface, self._hud_rect)