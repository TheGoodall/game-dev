
# Import Modules
import pygame

# Import game component
import DontWaitVaccinate.game as game

# Initialise game constants
FRAMERATE = 60
DEFAULT_SCREEN_RES = (1920, 1080)
PYGAME_FLAGS = pygame.SCALED
BACKGROUND_COLOUR = (0,0,0)

# Initialise Pygame and displays
pygame.init()
screen = pygame.display.set_mode(DEFAULT_SCREEN_RES, PYGAME_FLAGS)

# Initialise Font
font = pygame.font.SysFont("ubuntu", 35)

# Initialise clock
clock = pygame.time.Clock()

# Initialise Game
game_instance = game.game()

# Main Loop
while game_instance.running:

    # Tick clock at 60fps
    clock.tick(FRAMERATE)

    # Process events
    game_instance.loop(clock.get_time())

    # Clear screen
    screen.fill(BACKGROUND_COLOUR)

    # Render Game to surface
    game_instance.render(screen, font)

    # Scale surface and render to screen
    pygame.display.update()
