
# Import Modules
import pygame

# Import game component
import DontWaitVaccinate.game as game

# Initialise game constants
FRAMERATE = 60
RENDER_RES = (1280,720)
DEFAULT_SCREEN_RES = (1280,720)

# Initialise Pygame and displays
pygame.init()
screen = pygame.display.set_mode(DEFAULT_SCREEN_RES, pygame.RESIZABLE)
surface = pygame.Surface(RENDER_RES)

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
