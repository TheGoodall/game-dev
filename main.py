
# Import Modules
import pygame

# Import game component
import DontWaitVaccinate.game as game

# Initialise Pygame and displays
pygame.init()
screen = pygame.display.set_mode((480, 320), pygame.RESIZABLE)
surface = pygame.Surface((1280, 720))

# Initialise game constants
FRAMERATE = 60

# Initialise clock
clock = pygame.time.Clock()

# Initialise Game
game_instance = game.game()

# Main Loop
while game_instance.running:

    # Tick clock at 60fps
    clock.tick(FRAMERATE)

    # Process events
    game_instance.loop()

    # Render Game to surface
    game_instance.render(surface)

    # Scale surface and render to screen
    pygame.transform.scale(
        surface, (screen.get_width(), screen.get_height()), screen)
    pygame.display.update()
