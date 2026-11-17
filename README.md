# Rhythm Adventure

**Rhythm Adventure** is a 2D top-down RPG and 6-lane rhythm-battle hybrid built in Python using **Pygame Community Edition (`pygame-ce`)**. Explore the overworld as a slime hero, trigger interactive story encounters, and defend your HP in beat-synchronized rhythm combat.

---

## Features
* **Hybrid RPG + Rhythm Gameplay:** Seamless state transitions between a keyboard-driven Main Menu, 2D Overworld Exploration, 6-Lane Rhythm Boss Battles, and Victory/Game Over result screens.
* **Object-Oriented Architecture:** Built around an abstract `GameObject` base contract (`ABC`), encapsulated entity stats (`@property`), polymorphic update/draw dispatch loops, and sprite flipbook animation.
* **Real-Time Combat & Stakes:** Missing rhythm notes deducts HP from the Hero's health bar in real time, leading to a **Victory** screen upon clearing the beatmap or a **Game Over** screen if HP reaches `0`.
* **Performance Optimized:** Pre-renders static UI labels, caches scaled HUD portraits and combo counters, and uses `Vector2` normalized movement at a locked 60 FPS.

---

## Setup & Installation

### Prerequisites
* **Python 3.10+**
* **`pygame-ce`** (Pygame Community Edition)

### Installation & Run
1. Clone or download the repository and open the project folder in your terminal:
   ```bash
   cd RhythmAdventure-main
   ```
2. Create a Python virtual environment (`.venv`):
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   * **Windows (PowerShell / CMD):**
     ```bash
     .venv\Scripts\activate
     ```
   * **macOS / Linux:**
     ```bash
     source .venv/bin/activate
     ```
4. Install the required dependency inside the virtual environment:
   ```bash
   pip install pygame-ce
   ```
5. Launch the game:
   ```bash
   python main.py
   ```

---

## Controls

| Game State | Action | Key(s) |
| :--- | :--- | :--- |
| **Main Menu** | Move Selection Up / Down | `W` / `S` or `Up` / `Down` Arrows |
| **Main Menu** | Confirm Selection | `SPACE` or `ENTER` |
| **Overworld (`PLAYING`)** | Move Hero (8-directional normalized) | `W`, `A`, `S`, `D` |
| **Overworld (`PLAYING`)** | Interact / Start Rhythm Battle at Zone A | `SPACE` |
| **Rhythm Battle** | Left-Hand Note Lanes (Lanes 1–3) | `S`, `D`, `F` |
| **Rhythm Battle** | Right-Hand Note Lanes (Lanes 4–6) | `J`, `K`, `L` |
| **Victory / Game Over** | Restart Run | `R`, `SPACE`, or `ENTER` |
| **Global** | Return to Main Menu | `ESC` |

---

## Architecture & OOP Design

* **Abstract Base Class Contract (`game_object.py`):** `GameObject(ABC)` enforces `update(keys, events=None)` and `draw(screen)` across every entity, battle element, and UI screen.
* **Unified Polymorphic Dispatch (`main.py`):** Both overworld (`game_objects`) and combat (`battle_objects`) update and render their active objects through uniform polymorphic loops.
* **Inheritance:** `Entity` extends `GameObject`, and `Hero` extends `Entity` to inherit health/speed management and HUD rendering while adding collision physics and animation.
* **Encapsulation (`src/entity.py`, `src/rhythm_manager.py`):** Protected attributes (`_health`, `_speed`, `_score`, `_is_finished`) are managed via `@property` getters and clamping setters.
* **Composition & Association:** `Hero` owns an `Animator` instance (`1:1`), while `RhythmManager` manages spawned `Note` instances (`1:*`) and coordinates with `RhythmBoard` and `Hero`.

---

## Project Structure

```text
RhythmAdventure-main/
├── main.py                  # Main 60 FPS loop and state machine
├── game_object.py           # Abstract Base Class (GameObject)
├── README.md                # Setup instructions, controls, architecture & credits
├── AI_LOG.md                # Development and AI collaboration log
├── docs/
│   └── class-diagram.png    # UML class diagram
├── assets/
│   ├── beatmap_data.py      # Song note timestamps and lane choreography
│   ├── map_data.py          # Room backgrounds, walls, triggers, and BGM
│   ├── entities/            # Hero sprite frames
│   ├── music/               # Exploration and boss battle tracks
│   └── sound/               # Movement and hit-feedback sound effects
└── src/
    ├── animation.py         # Sprite flipbook animator
    ├── background.py        # Room background renderer
    ├── cutscene_manager.py  # Proximity trigger and battle transition handler
    ├── end_screen.py        # Victory and Game Over summary UI
    ├── entity.py            # Base entity class with encapsulated HP/speed HUD
    ├── hero.py              # Player movement, collision resolution, and SFX
    ├── loader.py            # Map, entity, and BGM loader helpers
    ├── menu.py              # Keyboard-controlled title screen
    ├── note.py              # Falling rhythm note entity
    ├── rhythm_board.py      # 6-lane highway and target catcher renderer
    ├── rhythm_manager.py    # Beatmap spawning, hit/miss scoring, and HP damage
    ├── textbox.py           # Overworld interaction prompt UI
    └── wasd_overlay.py      # On-screen movement key guide
```

---

## Assets & Credits

* **Music & Sound Effects:** Exploration BGM, boss battle music (`Boss_music.mp3`), movement SFX (`Slime_Move.mp3`), and UI/rhythm feedback SFX (`Click.mp3`) sourced from [Pixabay](https://pixabay.com/th/music/search/).
* **Character Artwork:** Slime hero animation frames (`Hero_idle.png`, `Hero_squeesh.png`) generated using **Google Flow**.
* **Background Artwork:** Base interior tileset sourced from [Winlu Fantasy Tileset - Interior](https://winlu.itch.io/winlu-fantasy-tileset-interior/devlog/683502/big-remaster-update) by **Winlu**, customized and modified using **Google Flow**.