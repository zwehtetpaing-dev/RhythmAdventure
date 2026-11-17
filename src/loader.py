import pygame
from src.hero import Hero
from src.background import Background
from assets.map_data import MAP_DATA


def play_room_music(room_name):
    """Loads and loops the background music assigned to a room, if any."""
    bgm_path = MAP_DATA[room_name].get("bgm_path")
    if bgm_path:
        pygame.mixer.music.load(bgm_path)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)


def load_map(room_name):
    room_info = MAP_DATA[room_name]

    obstacles = [pygame.Rect(coords) for coords in room_info["obstacles"]]
    cutscenes = [pygame.Rect(coords) for coords in room_info["cutscenes"]]
    background = Background(room_info["image_path"])

    play_room_music(room_name)
    return background, obstacles, cutscenes


def load_character(obstacles):
    """Spawns the hero with the current room's collision boxes."""
    return Hero("assets/entities/hero/Hero_idle.png", 500, 500, 3, 200, obstacles=obstacles)