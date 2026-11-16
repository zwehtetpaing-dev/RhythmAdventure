import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Set up the display window
WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")

# 3. Set up the clock for frame rate control
clock = pygame.time.Clock()
running = True

# 1. Create the invisible math boxes (Capital R!)
player_hitbox = pygame.Rect(50, 50, 40, 40)
boss_hitbox = pygame.Rect(70, 70, 40, 40)


rect_1 = pygame.Rect(0,0, 25, 25)

# 4. Main Game Loop
while running:
    # Event handling (check for window close button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here
    # 2. Check for the collision using only the invisible boxes
    if player_hitbox.colliderect(boss_hitbox):
        print("Collision happened!")

    # Rendering / Drawing
    screen.fill("black")  # Clear screen with a solid color

    # Update the full display surface to the screen
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

# 5. Clean up and exit
pygame.quit()