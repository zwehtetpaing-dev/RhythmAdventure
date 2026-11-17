import pygame
from src.hero import Hero
from src.background import Background
from assets.map_data import MAP_DATA

def load_map(room_name):
    room_info = MAP_DATA[room_name]

    # Build the walls and cutscenes
    obstacles = [pygame.Rect(coords) for coords in room_info["obstacles"]]
    cutscenes = [pygame.Rect(coords) for coords in room_info["cutscenes"]]

    # Paint the background
    background = Background(room_info["image_path"])

    # We check if the room has a song attached to it
    if "bgm_path" in room_info:
        pygame.mixer.music.load(room_info["bgm_path"])
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1) 

    return background, obstacles, cutscenes

def load_character(obstacles):
    """The casting director: brings the hero in and gives them the map's walls."""
    # Right now it just loads the Hero, but later you could pass in a 'character_name' 
    # to load different party members or enemies!
    hero = Hero("assets/entities/hero/Hero_idle.png", 500, 500, 3, 200, obstacles=obstacles)
    
    return hero