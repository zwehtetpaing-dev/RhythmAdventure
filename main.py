# Example file showing a basic pygame "game loop"
import pygame
from render.hero import Hero
from render.background import Background

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

##### Obstacle Hitbox Testing
Hitbox1 = pygame.Rect(0, 0, 326, 476)
Hitbox2 = pygame.Rect(326, 0, 194, 393)
Hitbox3 = pygame.Rect(726, 0, 194, 393)
Hitbox4 = pygame.Rect(920, 0, 359, 476)
Hitbox5 = pygame.Rect(0, 638, 64, 81)
Hitbox6 = pygame.Rect(1183, 638, 98, 81)
##### Cut scene hitbox
Hitbox7 = pygame.Rect(520, 0, 206, 318)
Hitbox8 = pygame.Rect(0, 476, 32, 162)
Hitbox9 = pygame.Rect(1248, 476, 32, 162)


# Create game objects
hero = Hero("assets/entities/hero/Hero.png", 100, 100, 3, 100)
background = Background("assets/background/Entrance.png")

# Unified polymorphic dispatch
game_objects = [background, hero]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # CHECK THE KEYS
    keys = pygame.key.get_pressed()
    
    # Update every object
    for obj in game_objects:
        obj.update(keys)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    for obj in game_objects:
        obj.draw(screen)

    ######## Test draw
    pygame.draw.rect(screen, "green", Hitbox1, 2)
    pygame.draw.rect(screen, "green", Hitbox2, 2)
    pygame.draw.rect(screen, "green", Hitbox3, 2)
    pygame.draw.rect(screen, "green", Hitbox4, 2)
    pygame.draw.rect(screen, "green", Hitbox5, 2)
    pygame.draw.rect(screen, "green", Hitbox6, 2)
    pygame.draw.rect(screen, "yellow", Hitbox7, 2)
    pygame.draw.rect(screen, "yellow", Hitbox8, 2)
    pygame.draw.rect(screen, "yellow", Hitbox9, 2)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()