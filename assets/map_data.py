# assets/map_data.py

# We group everything by the specific Map/Room name!
MAP_DATA = {
    "Entrance": {
        "image_path": "assets/background/Entrance.png",
        "bgm_path": "assets/music/Entrance_Theme.mp3",
        "obstacles": [
            (0, 0, 326, 476),
            (326, 0, 194, 393),
            (726, 0, 194, 393),
            (920, 0, 359, 476),
            (0, 638, 64, 81),
            (1183, 638, 98, 81)
        ],
        "cutscenes": [
            (520, 0, 206, 318),     # Cut scene hitbox
            (0, 476, 32, 162),
            (1248, 476, 32, 162)
        ]
    },
    
    "BossRoom": {
        "image_path": "assets/background/BossRoom.png",
        "bgm_path": "",
        "obstacles": [
            # DummySquare can drop the Boss Room wall coordinates here later!
        ],
        "cutscenes": [
            # Boss Room triggers can go here!
        ]
    }
}