# AI Collaboration Log (`AI_LOG.md`)

This document records how AI tools were used during the development, debugging, optimization, and documentation of **Rhythm Adventure** for the SF211 Term Project. All architectural decisions, asset integrations, and code changes were reviewed, tested, and verified by the team.

---

## 1. Summary of Original Team Work vs. AI Assistance
* **Original Team Design & Implementation:**
  * Designed the core hybrid concept combining a 2D top-down slime adventure with a 6-lane keyboard rhythm battle (`S D F J K L`).
  * Created the initial OOP hierarchy (`GameObject` ABC, `Entity`, `Hero`, `Animator`, `Background`, `CutsceneManager`, `TextBox`, `WASDOverlay`, `MainMenu`, `RhythmBoard`, `RhythmManager`, and `Note`).
  * Authored the room collision coordinates (`assets/map_data.py`), boss beatmap timing choreography (`assets/beatmap_data.py`), sprite artwork, and audio tracks.
* **AI-Assisted Debugging, Refactoring & Polish:**
  * Diagnosed state-reset bugs that prevented replaying battles or returning cleanly from the menu.
  * Fixed lane-matching and combo-reset logic in the rhythm hit detector.
  * Optimized rendering performance by moving font creation and surface scaling out of 60 FPS `draw()` loops.
  * Aligned all subclasses with strict `GameObject` polymorphism and added Victory/Game Over/Restart end conditions.

---

## 2. Detailed Interaction Log

### Session 1: Environment Setup & Initial Code Review
* **Goal:** Configure the local VS Code Python interpreter to run `main.py` and verify project structure.
* **Issue Encountered:** VS Code launched PowerShell with an empty interpreter string (`& '' main.py`) because no Python path was selected.
* **Resolution:** Selected the installed Python 3.14 interpreter with `pygame-ce` via the VS Code Command Palette (`Python: Select Interpreter`) and verified all `src/` imports.

### Session 2: Fixing Replay State Locks & Menu Controls
* **Goal:** Allow players to replay the boss rhythm battle multiple times and navigate menus smoothly.
* **Bugs Identified:**
  1. `RhythmManager` was instantiated only once at startup in `main.py`. After the first battle emptied `self.script` and set `is_finished = True`, re-entering Trigger Zone `A` immediately exited back to the overworld.
  2. `MainMenu.action` remained `"START"` after starting the game, causing `ESC` returns to immediately re-enter gameplay.
* **Code Changes Applied:**
  * Instantiated a fresh `RhythmManager` inside `main.py` whenever `cutscene_manager.action == "START_RHYTHM"` triggers.
  * Added `MainMenu.reset()` and expanded menu navigation to accept `Up`/`Down` arrows and `Enter` alongside `W`/`S` and `Space`.

### Session 3: Fixing Rhythm Lane Hit Detection & Combo Logic
* **Goal:** Ensure key presses (`S, D, F, J, K, L`) only evaluate notes in the corresponding lane.
* **Bug Identified:** `RhythmManager.update()` iterated through `self.active_notes` without filtering by lane, causing a tap in one lane to check the oldest note in a different lane and reset the player's combo prematurely.
* **Code Changes Applied:**
  * Added `self.lane` to `Note` (`src/note.py`).
  * Updated `RhythmManager._handle_lane_tap()` to filter `active_notes` by `note.lane == lane_idx` and evaluate the lowest note (`max(..., key=lambda n: n.y)`) closest to `target_y`.

### Session 4: Frame-Rate & Physics Optimization
* **Goal:** Eliminate redundant per-frame allocations and fix movement/setter bugs.
* **Code Changes Applied:**
  * **Font & Image Caching:** Moved `pygame.font.SysFont()` and `pygame.transform.scale()` calls out of `draw()` into `__init__` across `Entity`, `MainMenu`, `RhythmBoard`, and `RhythmManager`.
  * **Non-Blocking End-of-Song Transition:** Replaced `pygame.time.wait(1000)` in `main.py` with a 60-frame non-blocking timer inside `RhythmManager.update()`.
  * **Physics & Encapsulation Fixes:** Fixed `Entity.speed.setter` so it updates `self._speed`, clamped `Entity.health` to `[0, max_health]`, and normalized diagonal movement in `Hero.update()` using `pygame.math.Vector2.normalize()`.

### Session 5: Rubric Compliance (Polymorphism, End Conditions & Deliverables)
* **Goal:** Satisfy all SF211 rubric criteria for OOP contracts, end conditions, restart flow, and documentation.
* **Code Changes Applied:**
  * Updated `Note.update(self, keys, events=None)` with `sync_time()` so `main.py` dispatches all `battle_objects` polymorphically through the `GameObject` interface.
  * Connected missed rhythm notes to deduct HP from `Hero.health` (`miss_damage=20`) and added read-only `@property` metrics (`score`, `accuracy`, `is_finished`) to `RhythmManager`.
  * Created `src/end_screen.py` (`EndScreen`) to display **Victory** and **Game Over** results with `[R / Space]` restart support.
  * Created `README.md`, `AI_LOG.md`, and `generate_uml.py` to produce `docs/class-diagram.png`.

---

## 3. Oral Defense Verification
Every team member has reviewed the updated modules and can explain:
1. How `GameObject` enforces polymorphic `update()` and `draw()` calls in `main.py`.
2. How `@property` encapsulation in `Entity` and `RhythmManager` protects state invariants.
3. How audio timestamps (`pygame.mixer.music.get_pos()`) drive deterministic note positioning (`y = target_y - (target_time - current_time) * speed`) in `Note`.