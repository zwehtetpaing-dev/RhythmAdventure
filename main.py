# Example file showing a basic pygame "game loop"
import pygame
from hero import Hero
from background import Background

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

# hero
hero = Hero("assets/entities/hero/Hero.png", 100, 100, 3, 100)

# background
background = Background("assets/background/Entrance.png")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # CHECK THE KEYS
    keys = pygame.key.get_pressed()
    
    # This gives you that classic, smooth top-down RPG movement!
    hero.move(keys)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    background.draw(screen)
    hero.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()