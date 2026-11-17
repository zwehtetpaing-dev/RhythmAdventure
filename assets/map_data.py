# assets/map_data.py

# We store the coordinates as tuples: (x, y, width, height)
# Grouping them by room makes it super easy to load different maps later!
MAP_COLLISIONS = {
    "entrance_obstacles": [
        (0, 0, 326, 476),
        (326, 0, 194, 393),
        (726, 0, 194, 393),
        (920, 0, 359, 476),
        (0, 638, 64, 81),
        (1183, 638, 98, 81)
    ],
    "entrance_triggers": [
        (520, 0, 206, 318),     # Cut scene hitbox
        (0, 476, 32, 162),
        (1248, 476, 32, 162)
    ]
}