import pygame
from src.hero import Hero
from src.background import Background
from assets.map_data import MAP_DATA

def load_map(room_name):
    """The set builder: grabs the background and all the collision boxes."""
    room_info = MAP_DATA[room_name]

    # Build the physical walls
    obstacles = []
    for coords in room_info["obstacles"]:
        obstacles.append(pygame.Rect(coords))

    # Build the invisible triggers for cutscenes
    cutscenes = []
    for coords in room_info["cutscenes"]:
        cutscenes.append(pygame.Rect(coords))

    # Paint the background
    background = Background(room_info["image_path"])

    return background, obstacles, cutscenes


def load_character(obstacles):
    """The casting director: brings the hero in and gives them the map's walls."""
    # Right now it just loads the Hero, but later you could pass in a 'character_name' 
    # to load different party members or enemies!
    hero = Hero("assets/entities/hero/Hero_idle.png", 500, 500, 3, 200, obstacles=obstacles)
    
    return hero